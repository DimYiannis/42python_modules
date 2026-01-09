from .CardFactory import CardFactory
from ex1.SpellCard import Spell
from ex1.ArtifactCard import Artifact
from ex0.CreatureCard import Creature
from typing import Dict
import random

class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None):
        return Spell(""Lightning Bolt", 3, "Common", "damage"")

    def create_artifact(self, name_or_power=None):
        return Artifact("Mana Ring", 2, "Rare", 5, "+1 mana per turn")

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "Lightning"],
            "Artifacts": ["mana_ring"]
        }
