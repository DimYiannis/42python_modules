
from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory

if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")
 
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    turn = engine.simulate_turn()
    print("Turn execution:", turn)

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
