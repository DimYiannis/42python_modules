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

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_value,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.health, incoming_damage // 2)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        still_alive = self.health > 0
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_value, "health": self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losse": self.losses
        }
