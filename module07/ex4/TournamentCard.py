from ex0.Card import Card
from ex2.Combatable import Combatable
from Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    """
        class for a card that has
        abilities for combat and rank
    """
    def __init__(self, name:str, cost:int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack_value = attack
        self.health = health
        self.wins = 0
        self.losses =0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "effect": "Tournament card played"}
