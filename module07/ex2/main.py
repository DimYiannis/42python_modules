
from .EliteCard import EliteCard

if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")

    elite = EliteCard("Arcane Warrior", 6, "Legendary", attack_power = 5)

    print("\nEliteCard capabilities:")
    print("- Card:", [func for func in dir(EliteCard) if func in ["play", "get_card_info", "is_playable"]])
    print("- Compatable:", [func for func in dir(EliteCard) if func in ["attack", "defend", "get_combat_stats"]])
    print("- Magical:", [func for func in dir(EliteCard) if func in ["cast_spell", "channel_mana", "get_magic_stats"]])

    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defence result:", elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel", elite.channel_mana(3))

    print("\nMultiple interface implementation successful!!")
