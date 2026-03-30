from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===")
    factory = FantasyCardFactory(
        name="Fantasy Factory",
        types={
            "creatures": [
                "goblin",
                "dragon"
            ],
            "spells": [
                "fireball",
            ],
            "artifacts": [
                "mana_ring"
            ]
        }
    )
    strategy = AggressiveStrategy()
    game_engine = GameEngine()
    game_engine.configure_engine(factory, strategy)
    print("Available types:", factory.types)
    print("\nSimulating aggressive turn...")
    dragon = factory.create_creature("Fire Dragon")
    goblin = factory.create_creature("Goblin Warrior")
    lightning = factory.create_spell("Lightning Bolt")
    hand = [dragon, goblin, lightning]
    print("Hand:", [card.name + "(" + str(card.cost) + ")" for card in hand])
    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    turn_result = strategy.execute_turn(hand, ["Enemy Player"])
    print("Actions: ", turn_result)
    print("\nGame Report:")
    print(game_engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
