
from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")
 
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print("\nConfiguring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    enemy_targets = ["Goblin Warrior"]

    print("\nSimulating aggressive turn...")
    turn = engine.simulate_turn(enemy_targets)

    print("\nTurn execution:")
    print("Strategy:", turn["Strategy"])
    print("Actions:", turn["Actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
