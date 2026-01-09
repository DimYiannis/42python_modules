from .CreatureCard import CreatureCard

if __name__ == "__main__":

    print("=== DataDeck Card Foundation ===")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    
    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    avalaible_mana = 6
    print(f"\nPlaying Fire Dragon with {avalaible_mana} mana available:")
    print("Playable:", fire_dragon.is_playable(avalaible_mana))
    print("Play result:", fire_dragon.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")
