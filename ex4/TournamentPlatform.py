from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self, name: str) -> None:
        self.name = name
        self.registered_cards = []
        self.tournament_results = []

    def register_card(self, card: 'TournamentCard') -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("Only TournamentCards can be registered.")
        self.registered_cards.append(card)
        interfaces = [parent.__name__ for parent in card.__class__.__mro__
                      if parent not in (object, TournamentCard)
                      and parent.__name__ != 'ABC']
        return (f"{card.name} (ID: {card.id})\n"
                f"- Interfaces: {interfaces}\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.wins}-{card.losses}\n")

    def find_card_by_id(self, card_id: str) -> TournamentCard | None:
        return next(
            (card for card in self.registered_cards if card.id == card_id),
            None,
        )

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.find_card_by_id(card1_id)
        card2 = self.find_card_by_id(card2_id)
        if not card1 or not card2:
            raise ValueError("One or both cards not found.")

        card1_score = card1.attack_power + card1.health
        card2_score = card2.attack_power + card2.health

        if card1_score > card2_score:
            winner = card1
            loser = card2
        elif card2_score > card1_score:
            winner = card2
            loser = card1
        else:
            if card1.rating >= card2.rating:
                winner = card1
                loser = card2
            else:
                winner = card2
                loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        winner.rating += 16
        loser.rating = max(0, loser.rating - 16)
        result = {
            "winner_id": winner.id,
            "loser_id": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }
        self.tournament_results.append(result)
        return result

    def get_leaderboard(self) -> List:
        sorted_cards = sorted(
            self.registered_cards,
            key=lambda c: (c.rating, c.wins, -c.losses),
            reverse=True
        )
        leaderboard = []
        for c in sorted_cards:
            leaderboard.append(f"{c.name} - Rating: "
                               f"{c.rating} ({c.wins}-{c.losses})")
        return leaderboard

    def generate_report(self) -> Dict:
        rating = sum(card.rating for card in self.registered_cards)
        lenght = len(self.registered_cards) if self.registered_cards else 0
        return {
            "total_cards": lenght,
            "matches_played": len(self.tournament_results),
            "avg_rating": (rating / lenght) if lenght > 0 else 0,
            "platform_status": "Active"
            if self.registered_cards else "No cards registered",
        }
