from abc import ABC, abstractmethod
from ex0.CreatureCard import CreatureCard
from typing import Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, target: List[CreatureCard]) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
