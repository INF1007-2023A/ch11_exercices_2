"""
Chapitre 11

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *


# TODO: Créer la classe Spell qui a les même propriétés que Weapon, mais avec un coût en MP pour l'utiliser
class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name:      Le nom du sort
	:param power:     Le niveau d'attaque
	:param mp_cost:   Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	# TODO: __init__
	def __init__(self, name, power, mp_cost, min_level):
		super().__init__(name, power, min_level)
		self.mp_cost = mp_cost

	def is_usable_by(self, character):
		return isinstance(character, Magician) and super().is_usable_by(character)

	def compute_damage(self, user, opponent):
		return utils.compute_damage_output(
			user.level + user.magic_attack,
			self.power,
			1,
			1,
			1/8,
			(0.85, 1.00)
		)

# TODO: Déclarer la classe Magician qui étend la classe Character
class Magician(Character):
	"""
	Un utilisateur de magie dans le jeu. Un magicien peut utiliser des sorts, mais peut aussi utiliser des armes physiques. Sa capacité à utiliser des sorts dépend

	:param name:         Le nom du personnage
	:param max_hp:       HP maximum
	:param max_mp:       MP maximum
	:param attack:       Le niveau d'attaque physique du personnage
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param defense:      Le niveau de défense du personnage
	:param level:        Le niveau d'expérience du personnage

	:ivar using_magic: Détermine si le magicien tente d'utiliser sa magie dans un combat.
	"""

	def __init__(self, name, max_hp, max_mp, attack, magic_attack, defense, level):
		# TODO: Initialiser les attributs de Character
		super().__init__(name, max_hp, attack, defense, level)
		# TODO: Initialiser le `magic_attack` avec le paramètre, le `max_mp` et `mp` de la même façon que `max_hp` et `hp`, `spell` à None et `using_magic` à False.
		self.magic_attack = magic_attack
		self.__max_mp = max_mp
		self.mp = max_mp
		self.spell = None
		self.using_magic = False

	@property
	def max_mp(self):
		return self.__max_mp

	@max_mp.setter
	def max_mp(self, value):
		self.__max_mp = value
		self.mp = self.mp

	@property
	def mp(self):
		return self.__mp

	@mp.setter
	def mp(self, val):
		self.__mp = utils.clamp(val, 0, self.max_mp)

	# TODO: Écrire les getter/setter pour la propriété `spell`.
	#       On peut affecter None.
	#       Si le niveau minimal d'un sort est supérieur au niveau du personnage, on lève ValueError.
	@property
	def spell(self):
		return self.__spell

	@spell.setter
	def spell(self, val):
		if val is not None and not val.is_usable_by(self):
			raise ValueError()
		self.__spell = val

	# TODO: Surcharger la méthode `apply_turn`
	def apply_turn(self, opponent):
		# Si le magicien va utiliser sa magie (`will_use_spell()`):
		if self.will_use_spell():
			# Utiliser le sort magique et soustraire à son MP le coût du sort
			self.mp -= self.spell.mp_cost
			main_attack = self.spell
		# Sinon
		else:
			# Utiliser l'arme physique
			main_attack = self.weapon

		msg = f"{self.name} used {main_attack.name}\n"
		msg += main_attack.use(self, opponent)
		return msg

	def will_use_spell(self):
		return self.using_magic and self.spell is not None and self.mp >= self.spell.mp_cost

