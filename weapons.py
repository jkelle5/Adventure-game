

#Define classes for each weapon with predefined attributes. 

#Define more as needed
class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def createweapon(object,damage,durability):
       return object("scalpel", damage, durability)
       



class Sword(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)

class Bow(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)

class Scalpel(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)


class Gun(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)


class MorningStar(Weapon):
    def __init__(self, name, damage, durability):
        super().__init__(name, damage, durability)