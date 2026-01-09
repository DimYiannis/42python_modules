from .Card import Card

class Creature(Card):
    """
        creat a card.     
    """
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        """
        initialize
        """
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health can't have negative values")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """
        play the card, returns a dictionary
        copy the data so that multiple systems 
        may read the same game_state
        """
        game_state = game_state.copy()
        return {
        "card_played": self.name,
        "mana_used": self.cost,
        "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }


