from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...\n")
    tourment_platform = TournamentPlatform("Global Tournament")
    dragon_card = TournamentCard(
        id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Epic",
        attack_power=8,
        health=10,
        wins=0,
        losses=0,
        rating=1200
    )
    wizard_card = TournamentCard(
        id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        attack_power=6,
        health=8,
        wins=0,
        losses=0,
        rating=1150
    )
    print(tourment_platform.register_card(dragon_card))
    print(tourment_platform.register_card(wizard_card))
    print("\nCreating tournament match...")
    print("Match results: ",
          tourment_platform.create_match("dragon_001", "wizard_001"))
    print("\nTournament Leaderboard:")
    leaderboard = tourment_platform.get_leaderboard()
    i = 1
    for card in leaderboard:
        print(f"{i}. {card}")
        i += 1
    print("\nPlatform Report:")
    report = tourment_platform.generate_report()
    print(report)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
