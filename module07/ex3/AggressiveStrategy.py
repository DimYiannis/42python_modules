from .GameStrategy import GameStrategy
from typing import List, Dict

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, targets: List) -> Dict:
        played_cards = []
        mana_used = 0
        damage = 0
        target = targets[0]

        for card in sorted(hand, key=lambda c: c.cost):
            played_cards.append(card.name)
            mana_used += card.cost
            damage += 3

        return {
            "cards_played": played_cards,
            "mana_used": mana_used,
            "targets_attacked": [target],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return available_targets
