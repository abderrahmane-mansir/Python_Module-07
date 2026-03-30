from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class Rarity(str, Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    MYTHIC = "Mythic"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str | Rarity) -> None:
        self.name = name
        self.cost = cost
        if isinstance(rarity, Rarity):
            self.rarity = rarity
        elif isinstance(rarity, str):
            rarity_value = rarity.strip().lower()
            match = next(
                (
                    item for item in Rarity
                    if item.value.lower() == rarity_value
                ),
                None,
            )
            if match is None:
                raise ValueError("Invalid rarity value")
            self.rarity = match
        else:
            raise ValueError("Invalid rarity value")

    def play(self, game_state: Dict) -> Dict:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
