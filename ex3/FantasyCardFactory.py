from typing import Dict, List

from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import choice, randint


class FantasyCardFactory(CardFactory):
    DEFAULT_CREATURE_NAMES = [
        "Fire Dragon",
        "Goblin Warrior",
        "Shadow Wolf",
        "Stone Golem",
        "Forest Elf",
    ]
    DEFAULT_SPELL_NAMES = [
        "Arcane Burst",
        "Healing Light",
        "Lightning Bolt",
        "Frost Nova",
        "Curse of Weakness",
    ]
    DEFAULT_ARTIFACT_NAMES = [
        "Ancient Relic",
        "Phoenix Feather",
        "Moonblade",
        "Runic Shield",
        "Mana Crystal",
    ]
    DEFAULT_RARITIES = ["Common", "Rare", "Epic", "Legendary"]
    DEFAULT_SPELL_EFFECTS = ["Damage", "Heal", "Buff", "Debuff"]
    DEFAULT_ARTIFACT_EFFECTS = [
        "Permanent: +1 mana per turn",
        "Boosts creature attack by +2",
        "Reduces incoming damage by 1",
        "Draw one extra card each turn",
    ]
    created_cards_count = 0

    def __init__(self, name: str, types: Dict[str, List]) -> None:
        self.name = name
        self.types = {
            "creatures": types.get("creatures", self.DEFAULT_CREATURE_NAMES),
            "spells": types.get("spells", self.DEFAULT_SPELL_NAMES),
            "artifacts": types.get(
                "artifacts", self.DEFAULT_ARTIFACT_NAMES
            )
        }

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> CreatureCard:
        self.created_cards_count += 1
        if isinstance(name_or_power, str):
            name = name_or_power
            power = randint(1, 10)
        elif isinstance(name_or_power, int):
            creature_names = self.types.get(
                "creatures", self.DEFAULT_CREATURE_NAMES
            )
            name = choice(creature_names)
            power = name_or_power
        else:
            creature_names = self.types.get(
                "creatures", self.DEFAULT_CREATURE_NAMES
            )
            name = choice(creature_names)
            power = randint(1, 10)

        return CreatureCard(
            name=name,
            cost=randint(1, 8),
            rarity=choice(self.DEFAULT_RARITIES),
            attack=power,
            health=randint(power, power + 4),
        )

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> SpellCard:
        self.created_cards_count += 1
        spell_names = self.types.get("spells", self.DEFAULT_SPELL_NAMES)

        if isinstance(name_or_power, str):
            name = name_or_power
            cost = randint(1, 8)
        elif isinstance(name_or_power, int):
            name = choice(spell_names)
            cost = max(1, name_or_power)
        else:
            name = choice(spell_names)
            cost = randint(1, 8)

        return SpellCard(
            name=name,
            cost=cost,
            rarity=choice(self.DEFAULT_RARITIES),
            effect_type=choice(self.DEFAULT_SPELL_EFFECTS),
        )

    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> ArtifactCard:
        self.created_cards_count += 1
        artifact_names = self.types.get(
            "artifacts", self.DEFAULT_ARTIFACT_NAMES
        )

        if isinstance(name_or_power, str):
            name = name_or_power
            durability = randint(1, 6)
        elif isinstance(name_or_power, int):
            name = choice(artifact_names)
            durability = max(1, name_or_power)
        else:
            name = choice(artifact_names)
            durability = randint(1, 6)

        return ArtifactCard(
            name=name,
            cost=randint(1, 8),
            rarity=choice(self.DEFAULT_RARITIES),
            durability=durability,
            effect=choice(self.DEFAULT_ARTIFACT_EFFECTS),
        )

    def create_themed_deck(self, size: int) -> Dict:
        if size <= 0:
            raise ValueError("size must be a positive integer")

        creatures_count = max(1, size // 2)
        spells_count = max(1, size // 4)
        artifacts_count = size - creatures_count - spells_count
        if artifacts_count <= 0:
            artifacts_count = 1
            creatures_count = max(1, creatures_count - 1)

        creatures = [self.create_creature() for _ in range(creatures_count)]
        spells = [self.create_spell() for _ in range(spells_count)]
        artifacts = [self.create_artifact() for _ in range(artifacts_count)]
        deck = creatures + spells + artifacts

        return {
            "factory": self.name,
            "size": len(deck),
            "cards": deck,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": self.types.get(
                "creatures", self.DEFAULT_CREATURE_NAMES
            ),
            "spells": self.types.get("spells", self.DEFAULT_SPELL_NAMES),
            "artifacts": self.types.get(
                "artifacts", self.DEFAULT_ARTIFACT_NAMES
            )
        }
