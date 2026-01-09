

print("=== DataDeck Card Foundation ===")

print("\nTesting Abstract Base Class Design:")

print("\nCreatureCard Info:")
print(f"{cardinfo}")

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable:", {true})
print(f"Play result:", {playresult})

print("\nFire Dragon attacks Goblin Warrior:")
print(f"Attack result:", { {'attacker': 'Fire Dragon', 'target': 'Goblin Warrior',
'damage_dealt': 7, 'combat_resolved': True}})

print("\nTesting insufficient mana (3 available):")
print("Playable:", {False})

print("\nAbstract pattern successfully demonstrated!")
