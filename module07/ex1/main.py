from .Deck import Deck
from .SpellCard import Spell
from .ArtifactCard import Artifact
from ex0.CreatureCard import Creature

if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    deck = Deck()

    deck.add_card(Spell("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(Artifact("Mana Crystal", 2, "Rare", 5, "+1 mana per turn"))
    deck.add_card(Creature("Fire Dragon", 5, "Legendary", 7, 5))

    deck.shuffle()

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")
    while True:
        card = deck.draw_card()
        if not card:
            break
        print(f"\nDrew: {card.name} ({card.__class__.__name__})")
        print("Play result:", card.play({}))
    print("\nPolymorphism in action: Same interface, different card behaviors!")
