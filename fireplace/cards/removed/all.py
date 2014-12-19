"""
Cards removed from the game
"""

from ..utils import *


# Dagger Mastery
class CS2_083:
	def action(self):
		if self.hero.weapon:
			self.hero.weapon.buff("CS2_083e")
		else:
			self.hero.summon("CS2_082")

class CS2_083e:
	Atk = 1


# Adrenaline Rush
class NEW1_006:
	action = drawCard
	combo = drawCards(2)


# Bolstered (Bloodsail Corsair)
class NEW1_025e:
	Health = 1
