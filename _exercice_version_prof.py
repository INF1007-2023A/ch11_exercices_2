"""
Chapitre 11
"""


import math
from inspect import *

from game import *
from character import *
from _spells_version_prof import *


def simulate_battle():
	c1 = Character("Äpik", 500, 150, 70, 70)
	c2 = Character("Gämmör", 550, 100, 120, 60)
	
	bfg = SimpleDamagingMove("BFG", 100, 69)
	slingshot = SimpleDamagingMove("Slingshot", 80, 20)
	suck = DrainingMove("Big Sucky", 70, 0.5, 30)
	thiccer = IntensifyingMove("Thiccer and THICCER", 50, 5, 20)

	c1.main_move = bfg
	c2.main_move = suck
	c2.secondary_move = thiccer

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

