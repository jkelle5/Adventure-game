from sqlalchemy import MetaData, create_engine, Column, Text, String, Integer, DateTime, select

from sqlalchemy.orm import sessionmaker ,declarative_base
from flask_sqlalchemy import SQLAlchemy
import data






#Database variables
db_url = 'localhost:5432'
db_name = 'AdventureGame'
db_user = 'Asearl'
db_password = 'Type2Play'

#Connect to database through sqlalchemy
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    damage = Column(Integer)
    durability = Column(Integer)

    def __init__(self, name, damage, durability):

        self.name = name
        self.damage = damage
        self.durability = durability

Base.metadata.create_all(engine)
print("done")

for weapon_data in data.weapons_data:
   
    
    session.add(Weapon(name=weapon_data['name'], damage=weapon_data['damage'], durability=weapon_data['durability']))

    # Commit the changes to the database
session.commit()
print("commited")

    # Close the session
session.close()