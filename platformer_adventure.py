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

    show_level_info(CURRENT_LEVEL)
    
    print("\nWhat will you do?")
    print("1. Jump over obstacles")
    print("2. Collect items")
    print("3. Stomp an enemy")
    print("4. Advance to next level")
    print("5. Check status")
    
    choice = input("Enter choice (1-5): ").strip()   # User Interaction
    
    # Control Flow - if, elif, else
    if choice == '1':
        print("Great jump! +10 Score")
        SCORE += 10
    elif choice == '2':
        # Using list methods
        if levels[CURRENT_LEVEL]["items"]:
            item = levels[CURRENT_LEVEL]["items"].pop(0)
            inventory.append(item)          # List method: append()
            print(f"Collected {item}! +20 Score")
            SCORE += 20
        else:
            print("No more items here!")
    elif choice == '3':
        if levels[CURRENT_LEVEL]["enemies"]:
            enemy = levels[CURRENT_LEVEL]["enemies"].pop(0)
            print(f"Stomped {enemy}! +15 Score")
            SCORE += 15
        else:
            print("No enemies left!")
    elif choice == '4':
        if CURRENT_LEVEL < len(levels):
            CURRENT_LEVEL += 1
            print(f"🎮 Advancing to Level {CURRENT_LEVEL}!")
        else:
            print("You've cleared all demo levels!")
    elif choice == '5':
        display_status()
    else:
        print("You tripped! -5 Health")
        HEALTH -= 5


def main():
    """Main game loop - demonstrates Iteration (while loop)."""
    global HEALTH
    print("=== Welcome to Text-Based Platformer Adventure! ===")
    print(f"You are {PLAYER_NAME}. Jump, collect, and conquer!\n")
    
    # Iteration: while loop for game loop
    while HEALTH > 0:
        display_status()
        explore_level()
        
        if SCORE >= 100:        # Control Flow
            print("\n🎉 CONGRATULATIONS! You mastered the platformer demo!")
            break