"""
Text Based Platformer Adventure (Mario)
Author: Hriday Vermani
Purpose: Simple text-based platformer style game using only Chapters 1-7 concepts.
Date: June 23 2026
"""
# === Variables & Simple Data Types ===
PLAYER_NAME = "Mario"           # String
HEALTH = 100                    # Integer
SCORE = 0                       # Integer
CURRENT_LEVEL = 1               # Integer
GAME_RUNNING = True             # Boolean
# List - stores player's collected items (ordered)
inventory = []

# Dictionary - stores level data with keys for easy lookup
levels = {      
    1: {
        "name": "Green Hills",
        "description": "Sunny hills with pipes and floating coins.",
        "enemies": ["Goomba", "Koopa"],      # List inside dictionary
        "items": ["Coin", "Mushroom"]        # List inside dictionary
    },
    2: {
        "name": "Underground Cave",
        "description": "Dark tunnels full of hidden treasures.",
        "enemies": ["Piranha Plant"],
        "items": ["Fire Flower"]
    }
}

def display_status():
    """Display current player status."""
    print(f"\n=== {PLAYER_NAME}'s Status ===")
    print(f"Health: {HEALTH} | Score: {SCORE} | Level: {CURRENT_LEVEL}")
    # Using list to show inventory
    print(f"Inventory: {inventory if inventory else 'Empty'}")

    def show_level_info(level):
       """Show details about the current level."""
    if level in levels:  # Control Flow (if statement)
        lvl = levels[level]
        print(f"\n--- Level {level}: {lvl['name']} ---")
        print(lvl["description"])
        print(f"Enemies: {', '.join(lvl['enemies'])}")
        print(f"Items: {', '.join(lvl['items'])}")
    else:
        print("Unknown level!")
        def explore_level():
         """Handle player actions in the current level."""
    global HEALTH, SCORE, CURRENT_LEVEL   # Modifying global variables