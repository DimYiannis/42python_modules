from typing import Dict, List
from .TournamentCard import TournamentCard

class TournamentPlatform:
    """
        manager for tournament cards, 
        matches and leaderboard
    """
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().replace(" ", "_") + f"_{len(self.cards)+1:03d}"
        self.cards[card_id] = card
        print(f"{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]

        if c1.attack_value >= c2.attack_value:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        lose.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.name.lower().replace(" ", "_"),
            "loser": losser.name.lower().replace(" ", "_"),
            "winner_rating": winner.rating,
            "loser_rating": losses.rating
        }

    def get_leaderboard(self) -> List[str]:
        sorted_cards = sorted(self.cards.values(), key=lambda c: c.rating, reverse=True)
        leaderboard = [
            f"{i + 1}. {c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
            for i, c in enumerate(sorted_cards)
        ]
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = sum(c.rating for c in self.cards.values())
        avg_rating = total_rating // len(self.cards) if self.cards else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }

