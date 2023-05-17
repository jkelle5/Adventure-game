import sys
import time
import os
import random

begin = input("Adventure Game \nStart or Leave\n").lower().strip()

if begin == "start":

    class items:
        def __init__(self, name, value, quantity=1):
            self.name = name
            self.value = value
            self.quantity = quantity

        pass


    class weapons:
        def __init__(self, name, value, damage, quantity=1):
            self.name = name
            self.value = value
            self.damage = damage
            self.quantity = quantity

            pass

    def createweapon():
        weapon = weapons("scalpel", 2, 1)
        print(weapon)
    #def scalpel(weapons):
        #name = "Scalpel"
        #value = 2
        #damage = 1
#scalpel = "scalpel",2,1

    print("\nAdventure Game\n\n\nThe world has become a desolate place\nA land Divided\nAnd a newcomer has found their "
          "way into this broken world.\n")
    print("Darkness...followed by a ringing in your ears and a head-splitting pain in the back of your skull.\n"
          "The ringing subsides and you realise you're laying down. You can feel a stiff cot beneath you.\n"
          "The center of the darkness turns to gray then to white as you realise you're looking up into a light.\n")

    C1 = input("Do you continue to stare into the light? (Yes or No)\n").lower().strip()

    if C1 == "no":

        print("You look to the left and your vision begins to come into focus. As you scan your surroundings you see\n"
              "that you are in what looks like a surgical room; you are laying on a stiff piece of canvas supported\n"
              "by metal bars in the center of the room to your right is a wall with grimy monitors showing different\n"
              "scans that you can't make sense of. the walls in front and behind you are barren and the wall to your\n"
              "has a single metal door set in the center. Just to the left of your bed is a cart full of surgical \n"
              "equipment. While taking in your surroundings you can hear muffled voices on the other side of the door.")

        C2 = input("\nWhat would you like to do? (inspect cart, attempt to eavesdrop, or try the door)\n").lower()

        if C2 == "inspect cart":
            print("Upon further inspection you see some bloody surgical tools on the top of the cart though you don't\n"
                  "notice any cuts on your body or pains except for your headache. Among the tools you see a scalpel\n"
                  "and surgical scissors. You find in one of the drawers a a syringe with a greenish yellow liquid \n"
                  "in it.\n")

            c2_1 = input("\nWhat would you like to do? (take scalpel, inject myself, or leave cart)\n").lower()
            while c2_1 != "leave cart":
                c2_2 = "0"
                c2_3 = "0"
                if c2_1 == "take scalpel":
                    print("\nYou now have a scalpel.\n")
                    createweapon()
                    print(weapons.name)
                    c2_2 = "1"
                elif c2_1 == "inject myself":
                    print("You stick the needle of the syringe into your thigh and press down on the plunger. As you\n"
                          "do you feel an intense burning radiating out from the injection point to the rest of your\n"
                          "body. As the burning subsides you feel stronger but your mind also feels cloudy.")
                    c2_3 = "1"
                if c2_2 and c2_3 == "1":
                    break

    else:
        print("Your headache gets worse and your vision immediately goes dark. After a period of time you hear a "
              "crashing sound in the adjacent room followed by yelling \nscreaming and gunfire. The gunfire subsides "
              "and you hear mumbling. You hear a door open followed by a gruff voice saying 'Damn looks like the old "
              "man did\nit, good thing we already took care of him' A second voice laughs then says 'Yeah the old "
              "bastard put up a real fight too. Too bad his little experiment\ndoesn't seem to be able to have vision."
              "'\n\nYou hear the cocking of a gun followed by the crack of a gunshot; then nothing.")
        print("\n\nYOU HAVE DIED\n\nGame Over")
else:
    print("Goodbye")
