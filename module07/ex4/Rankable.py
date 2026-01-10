from abc import ABC, abstractmethod

class Rankable(ABC):
    """
    abstract class for cards with rank
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """current rating of the card."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """number of wins."""
        pass

    @abstractmethod
    def  update_losses(self, losses: int) -> None:
        """number of losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """dictionary with rating, wins, and losses."""
        pass


















