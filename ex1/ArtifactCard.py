from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        if not self.is_playable(game_state.get("player_mana", 0)):
            raise ValueError("Not enough mana to play this card.")
        game_state["player_mana"] -= self.cost
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }
        return result

    def activate_effect(self) -> Dict:
        if self.durability <= 0:
            raise ValueError("This artifact is broken ")
        self.durability -= 1
        result = {
            "card_effect_activated": self.effect,
            "durability_remaining": self.durability
        }
        return result

    def get_card_info(self):
        info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "card_type": "Artifact",
            "durability": self.durability,
            "effect": self.effect
        }
        return info
