from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print(f"Configuring {factory.name}...")
        print(f"Factory {factory.__class__.__name__}")
        print(f"Strategy {strategy.get_strategy_name()}...")

    def simulate_turn(self) -> Dict:
        print("Strategy:", self.strategy.get_strategy_name())
        return self.strategy.execute_turn(
            self.factory.create_themed_deck(2), ["Enemy Player"])

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.strategy.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.strategy.total_damage_dealt,
            "cards_created": self.factory.created_cards_count
        }
