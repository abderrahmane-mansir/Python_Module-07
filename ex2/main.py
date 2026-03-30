from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical
from ex0.Card import Card


def main():
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    card_methods = [attribute for attribute in dir(Card)
                    if callable(getattr(Card, attribute))
                    and not attribute.startswith("__")]
    print("- Card:", card_methods)

    combatable = [attribute for attribute in dir(Combatable)
                  if callable(getattr(Combatable, attribute))
                  and not attribute.startswith("__")]
    print("- Combatable:", combatable)

    magical = [attribute for attribute in dir(Magical)
               if callable(getattr(Magical, attribute))
               and not attribute.startswith("__")]
    print("- Magical:", magical)

    elite_card = EliteCard(
        name="Arcane Warrior",
        rarity="Mythic",
        cost=8,
        attack_power=5,
        magic_power=4
    )
    game_state = {
        "player_mana": 10,
        "target": "Enemy",
        "targets": ["Enemy1", "Enemy2"],
        "damage": 5,
        "spell_name": "Fireball",
        "mana_amount": 3
    }
    card_info = elite_card.get_card_info()
    print(f"\nPlaying {elite_card.name} ({card_info['type']}):")
    result = elite_card.play(game_state)
    print("\nCombat phase:")
    print("Attack result:", result["attack"])
    print("Defend result:", result["defend"])
    print("\nMagic phase:")
    print("spell cast:", result["cast spell"])
    print("Mana channel:", result["channel mana"])
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
