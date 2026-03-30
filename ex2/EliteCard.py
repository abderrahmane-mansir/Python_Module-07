from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, magic_power: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.magic_power = magic_power

    def play(self, game_state: dict) -> Dict:
        result = {
            "attack": self.attack(game_state.get("target")),
            "defend": self.defend(game_state.get("damage")),
            "cast spell": self.cast_spell(game_state.get("spell_name"),
                                          game_state.get("targets")),
            "channel mana": self.channel_mana(game_state.get("mana_amount"))
        }
        return result

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Elite Card",
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
            }

    def defend(self, incoming_damage: int) -> Dict:
        armor = 3
        reached_damage = incoming_damage - armor
        return {
            "defender": self.name,
            "damage_taken": reached_damage,
            "damage_blocked": armor,
            "still_alive": True if reached_damage < 10 else False
            }

    def get_combat_stats(self) -> Dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power
            }

    def cast_spell(self, spell_name: str, target: List) -> Dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "target": target,
            "mana_used": len(target) * 2,
            }

    def channel_mana(self, amount: int) -> Dict:
        return {
            "channeled": amount,
            "total_mana": amount + self.magic_power
            }

    def get_magic_stats(self) -> Dict:
        return {"name": self.name, "magic_power": self.magic_power}
