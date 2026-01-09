from ex0.Card import Card
from typing import List, Dict

class SpellCard(Card)
    """
    class that inherits from card 
    class and represents a spell.
    """
    def __init__(self, name:str, cost:int, rarity:str, effect_type: str):
    super().__init__(name, cost, rarity)
    self.effect_type = effect_type
    self.consumed = False

    def play(self, game_state: Dict) -> Dict:
        """
        play the spellcard, do the changes and consume the spell at the end
        """
        if self.consumed:
            return {"card_played": self.name, "effect": "already used"}
        self.consumed = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal 3 {self.effect_type} to target"
        }
    def resolve_effect(self, targets: List[str]) -> Dict:
        """
        apply the spell to a list of targets
        """
        return {"target": targets, "effect_type": self.effect_type}
    
