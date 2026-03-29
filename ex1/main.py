from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation - SpellCard Testing ===")
    print("\nBuilding deck with different card types...")
    game_status = {
        "player_health": 30,
        "opponent_health": 30,
        "player_mana": 10,
        "opponent_mana": 6
    }
    lightning_bolt_spell = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="Damage"
    )
    mana_crystal_artifact = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=3,
        effect="Permanent: +1 mana per turn"
    )
    fire_dragon_card = CreatureCard(
                    name="Fire Dragon",
                    cost=5,
                    rarity="Legendary",
                    attack=7,
                    health=5
                    )
    deck = Deck(cards=[
        lightning_bolt_spell,
        mana_crystal_artifact,
        fire_dragon_card])
    print("Deck stats: ", deck.get_deck_stats())
    print("\nDrawing and playing cards:")
    deck.shuffle()
    for _ in range(len(deck.cards)):
        drawn_card = deck.draw_card()
        print(f"\nDrew card: {drawn_card.name} ({type(drawn_card).__name__})")
        print(f"Play result: {drawn_card.play(game_status)}")
    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
