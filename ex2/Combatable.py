from abc import ABC, abstractmethod
from ex0.CreatureCard import CreatureCard
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: CreatureCard) -> Dict:
        pass

    @abstractmethod
    def defend(self, damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
