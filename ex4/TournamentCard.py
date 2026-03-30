from ex0.Card import Card
from ex2.Combatable import Combatable
from ex0.CreatureCard import CreatureCard
from ex4.Rankable import Rankable

from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        wins: int = 0,
        losses: int = 0,
        rating: int = 0
    ) -> None:
        self.id = id
        super().__init__(name, cost, rarity)
        if attack_power <= 0 or health <= 0:
            raise ValueError("attack_power and health must be positive")
        self.attack_power = attack_power
        self.health = health
        self.wins = max(0, wins)
        self.losses = max(0, losses)
        self.rating = max(0, rating)

    def play(self, game_state: Dict) -> Dict:
        if not self.is_playable(game_state.get("player_mana", 0)):
            raise ValueError("Not enough mana to play this card.")
        game_state["player_mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the arena",
        }

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Tournament",
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def attack(self, target: CreatureCard) -> Dict:
        if not isinstance(target, CreatureCard):
            raise ValueError("Target must be a CreatureCard.")
        target.health = max(0, target.health - self.attack_power)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack_power,
            "target_remaining_health": target.health,
        }

    def defend(self, damage: int) -> Dict:
        if damage < 0:
            raise ValueError("damage must be non-negative")
        self.health = max(0, self.health - damage)
        return {
            "defender": self.name,
            "damage_taken": damage,
            "remaining_health": self.health,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> Dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
        }

    def calculate_rank(self) -> int:
        return max(0, self.wins * 3 - self.losses)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins increment must be non-negative")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses increment must be non-negative")
        self.losses += losses

    def get_rank_info(self) -> Dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rank": self.calculate_rank(),
        }
