from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers.")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        if not self.is_playable(game_state.get("player_mana", 0)):
            raise ValueError("Not enough mana to play this card.")
        game_state["player_mana"] -= self.cost
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return result

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def attack_target(self, target: 'CreatureCard') -> Dict:
        if not isinstance(target, CreatureCard):
            raise ValueError("Target must be a CreatureCard.")
        combat = True if self.attack > target.health else False
        target.health -= self.attack
        if target.health <= 0:
            target.health = 0
        result = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            'combat_resolved': combat
        }
        return result
