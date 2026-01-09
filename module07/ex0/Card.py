
from abc import ABC, abstractmethod
class Card(ABC):
    """
    base class to represent a card in the game
    """
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        play the card in a given game state
        to be implemented by subclasses
        """
        pass

    def get_card_info(self) -> dict:
        """
        return basic info about the card
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        check if a card is playable with the mana that we have
        """
        return available_mana >= self.cost
