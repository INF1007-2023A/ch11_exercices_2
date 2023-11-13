"""
Chapitre 11
"""


import math
from inspect import *

from game import *
from _magician_version_prof import *


def simulate_battle():
	c1 = Character("Äpik", 500, 150, 70, 70)
	c2 = Character("Gämmör", 550, 100, 120, 60)
	c3 = Magician("Damn! That magic dude", 450, 100, 50, 150, 50, 65)
	w1 = Weapon("BFG", 100, 69)
	w2 = Weapon("Deku Stick", 120, 1)
	w3 = Weapon("Slingshot", 80, 20)
	s1 = Spell("Big Chungus Power", 100, 35, 50)

	c1.weapon = w1
	c2.weapon = w2
	c3.spell = s1
	c3.weapon = w3
	c3.using_magic = True

	turns = run_battle(c3, c1)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

