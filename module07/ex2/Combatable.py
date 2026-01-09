
from abc import ABC, abstractmethod
from typing import Dict

class Combatable(ABC):
    """
     abstract base class for combat abilities
    """
    @abstractmethod
    def attack(self, targets) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
