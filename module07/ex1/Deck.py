from typing import List, Dict
from ex0.Card import Card
import random

class Deck:
    """
    manage different card types
    """
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card.name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0) if self.cards else None

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        creatures = sum(1 for c in self.cards 
            if c.__class__.__name__ == "Creature")
        spells = sum(1 for c in self.cards
            if c.__class__.__name__ == "Spell")
        artifacts = sum(1 for c in self.cards
            if c.__class__.__name__ == "Artifact")
        avg_cost = sum(c.cost for c in self.cards) / total if total > 0 else 0
        return {
           "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost 
        }




