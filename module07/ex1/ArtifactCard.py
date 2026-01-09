
from ex0.Card import Card
from typing import Dict

class Artifact(Card):
    def __init__(self, name:str, cost: int, rarity: str, durability:int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        """
        put artifact in the game,
        an artifact remains till its destroyed
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict:
        """
        activate ability for artifact
        """
        return {"artifact": self.name, "effect": self.effect, "durability": self.durability}

