from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import List, Dict
from random import shuffle
from math import ceil


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards: List[Card] = cards

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("Only Card instances can be added to the deck.")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        raise ValueError(f"Card with name '{card_name}'"
                         " not found in the deck.")

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty. Cannot draw a card.")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        creature_count = sum(isinstance(card, CreatureCard)
                             for card in self.cards)
        spell_count = sum(isinstance(card, SpellCard)
                          for card in self.cards)
        artifact_count = sum(isinstance(card, ArtifactCard)
                             for card in self.cards)
        stats = {
            "total_cards": len(self.cards),
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": float(
                ceil(sum(card.cost for card in self.cards) / len(self.cards))
            )
        }
        return stats
