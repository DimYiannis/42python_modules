
from ex0.Card import Card
from .Compatable import Compatable
from .Magical import Magical
from typing import List, Dict

class EliteCard(Card, Compatable, Magical):
    """
    class that combines combat
    and magical abilities
    """
    def __init__(self, name: str, cost: int, rarity:str, attack_power: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = 10
        self.mana = 0

    def play(self, game_state: Dict) -> Dict:
        return {"card_played": self.name, "mana_used": self.cost, "effect": "Elite card enters the battlefield"}

    def attack(self, target) -> Dict:
        return {"attacker": self.name, "target": target, "damage": self.attack_power, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(3, incoming_damage)
        self.health -= (incoming_damage - blocked)
        still_alive = self.health > 0
        return {"defender": self.name, "damage_taken": incoming_damage - blocked, "damage_blocked": blocked, "still_alive": still_alive}

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_power, "health": self.health}

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_cost = 4
        self.mana -= mana_cost
        return {"caster": self.name, "spell": spell_name, "targets": targets, "mana_used": mana_cost}

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict:
        return {"mana": self.mana}
