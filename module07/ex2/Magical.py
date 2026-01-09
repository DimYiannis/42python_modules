from abc import ABC, abstractmethod
from typing import List, Dict

class Magical(ABC):
    """
     abstract base class for magical abilities
    """
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
