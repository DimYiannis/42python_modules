
from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

if __name__ == "__main__":

    print("\n=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...\n")

    platform = TournamentPlatform()

    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    ice_wizard = TournamentCard("Ice Wizard", 4, "Epic", 6, 4)

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)
    
    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", match_result)


    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(entry)

    print("\nPlatform Report")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

