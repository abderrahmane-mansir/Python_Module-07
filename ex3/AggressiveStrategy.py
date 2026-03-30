from typing import Dict, List

from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    turns_simulated = 0
    total_damage_dealt = 0

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        self.turns_simulated += 1
        self.total_damage_dealt += sum(card.attack for card in hand
                                       if isinstance(card, CreatureCard))
        action = {
            "cards_played": [card.name for card in hand],
            "mana_used": sum(card.cost for card in hand),
            "targets_attacked": [creature for creature in battlefield],
            "damage_dealt": self.total_damage_dealt
        }
        return action

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        result = [target for target in available_targets if target.health < 5]
        return result
