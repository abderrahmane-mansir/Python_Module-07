from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    @abstractmethod
    def get_card_info(self) -> Dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
