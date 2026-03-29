from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    game_status = {
        "player_health": 30,
        "opponent_health": 30,
        "player_mana": 6,
        "opponent_mana": 6
    }
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    fire_dragon_card = CreatureCard(
                    name="Fire Dragon",
                    cost=5,
                    rarity="Legendary",
                    attack=7,
                    health=5
                    )
    print(fire_dragon_card.get_card_info())
    print(f"\nPlaying {fire_dragon_card.name} with "
          f"{game_status['player_mana']} mana available:")
    print("Playable: ",
          fire_dragon_card.is_playable(game_status["player_mana"]))
    print("Play result: ", fire_dragon_card.play(game_status))
    goblin_warrior_card = CreatureCard(
                    name="Goblin Warrior",
                    cost=3,
                    rarity="Common",
                    attack=4,
                    health=5
                    )
    print(f"\n{fire_dragon_card.name} attacks {goblin_warrior_card.name}:")
    print("Attack results: ",
          fire_dragon_card.attack_target(goblin_warrior_card))
    game_status["player_mana"] = 3
    print("\nTesting insufficient mana "
          f"({game_status['player_mana']} available):")
    print("Playable: ",
          fire_dragon_card.is_playable(game_status["player_mana"]))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
