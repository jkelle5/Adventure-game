

import data
import main
import models
from sqlalchemy import DateTime

#Must be run as a script in order to populate database. For development purposes only. Production should have a persisted database. 

# if needed, generate database schema
session = models.Session()


@main.cli.command("recreate")
def recreate_db():
    models.Base.metadata.drop_all(models.engine)
    models.Base.metadata.create_all(models.engine)

@main.cli.command("create_db")
def create_db():
    models.Base.metadata.create_all(models.engine)

@main.cli.command("seed_db")
def seed_db():
    # Add the weapons_data to the database
    for weapon_data in data.weapons_data:
        weapon = models.Weapon(name=weapon_data['name'], damage=weapon_data['damage'], durability=weapon_data['durability'])
        session.add(weapon)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main.cli()
