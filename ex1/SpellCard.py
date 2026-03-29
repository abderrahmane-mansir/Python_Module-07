from ex0.Card import Card
from typing import Dict


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.consumed = True
        if effect_type.lower() not in ["damage", "heal", "buff", "debuff"]:
            raise ValueError("Invalid effect type for SpellCard.")
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        if not self.consumed:
            raise ValueError("This spell card has already been used.")
        self.consumed = False
        if not self.is_playable(game_state.get("player_mana", 0)):
            raise ValueError("Not enough mana to play this card.")
        game_state["player_mana"] -= self.cost
        effects = ""
        if self.effect_type == "Damage":
            effects = f"Deals {self.cost} damage to opponent."
        if self.effect_type == "Heal":
            effects = f"Heals player for {self.cost} health."
        if self.effect_type == "Buff":
            effects = f"Buffs a creature for +{self.cost} attack"
        if self.effect_type == "Debuff":
            effects = f"Debuffs an opponent's creature for -{self.cost} attack"
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effects
        }
        return result

    def resolve_effect(self,  targets: list) -> Dict:
        result = {
            "card_effect_resolved": self.effect_type,
            "game_state_updated": True
        }
        return result

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Spell",
            "effect_type": self.effect_type
        }
