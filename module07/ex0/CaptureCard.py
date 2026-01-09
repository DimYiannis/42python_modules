from .Card import Card

class CaptureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int)
    


    @abstractmethod
    def play(self, game_state: dict) -> dict
    


    def attack_target(self, target) -> dict
