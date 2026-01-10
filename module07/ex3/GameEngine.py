from typing import Dict, List
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy

class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self, targets: List[str] | None = None) -> Dict:
        """
            - create cards
            - ask the strategy what to do
            - execute it
            - record the result 
            - and report what happened.
        """
        self.turns += 1

        hand = [
            self.factory.create_creature(),
            self.factory.create_spell(),
            self.factory.create_artifact()
        ]

        print("Hand:", [f"{card.name} ({card.cost})"
                    for card in hand
        ])

        if targets is None:
            targets = ["Enemy Player"]

        prioritized = self.strategy.prioritize_targets(targets)
        result = self.strategy.execute_turn(hand, prioritized)

        self.total_damage += result["damage_dealt"]

        return {
            "Strategy": self.strategy.get_strategy_name(),
            "Actions": result
        }

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": 3
        }
