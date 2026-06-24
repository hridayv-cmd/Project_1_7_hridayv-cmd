"""
Zombie apocalypse game
Author: Hriday Vermani
Purpose: Simple text-based zombie apocalsype game using Chapters 1-7 concepts.
Date: June 23 2026
"""
# 1. Variables & Simple Data Types
NAME = "Base One"
days = 0
scrap = 40
integrity = 100
running = True
successful_escape = False

# 2. Collections
survivors = ["Alice", "Bob", "Charlie"]  # List
resources = {"Food": 10, "Turrets": 1}   # Dictionary

print(f"=== Welcome to {NAME} ===")

#3 Main While Loop
while running and integrity > 0:
    days += 1
    print(f"\nDay {days} | Scrap: {scrap} | Integrity: {integrity}% | Team: {survivors}")
    
    print("1. Scavenge Supply | 2. Upgrade Turrets | 3. Abandon Base")
    choice = input("Your Command (1-3): ").strip()
# 4. Control Flow & User Interaction
    if choice == "1":
        if survivors:
            scrap += 20
            resources["Food"] += 5
            print("Success: Safe return! +20 Scrap, +5 Food.")
        else:
            print("Error: No survivors left to send out!")
            
    elif choice == "2":
        if scrap >= 25:
            scrap -= 25
            resources["Turrets"] += 1  # Modifying Dictionary
            print(f"Upgrade: Turrets upgraded to Level {resources['Turrets']}!")
        else:
            print("Error: Not enough scrap metal!")
    elif choice == "3":
        print(f"\nNotice: You abandoned {NAME}!")
        if days >= 11:
            print("Good ending! You selected the right time to exit and move to a new base.")
            successful_escape = True
        else:
            print(f"Bad ending! You abandoned the base on Day {days}. You could have survived longer instead of staying there for a short time and risking moving around during a horde.")
            successful_escape = False  # Left too early, considered a failure
        running = False
        break
    else:
        print("Warning: Invalid command! Day wasted.")
        # 5. NEW CHALLENGE MECHANICS
        # Zombie power scales up by 3 every single day
    zombie_attack_power = 15 + (days * 3)
    damage = zombie_attack_power - (resources["Turrets"] * 6)
    
    if damage > 0:
        integrity -= damage
        print(f"Alert: Zombies attacked with {zombie_attack_power} power! Base took {damage} damage.")
    else:
        print("Defense: Turrets wiped out the horde perfectly!")


    # New Food Consumption & Starvation Rule (Replaces your old food line!)
    food_needed = len(survivors) * 2
    if resources["Food"] >= food_needed:
        resources["Food"] -= food_needed
    else:
        resources["Food"] = 0
        if survivors:
            lost_survivor = survivors.pop()  # Removes the last person from the list
            print(f"CRITICAL: Starvation! {lost_survivor} ran out of food and perished.")

# 6. Game end code
print(f"\n=== GAME OVER ===")
if integrity <= 0:
    print("Reason: The base walls collapsed under the zombie horde.")
elif len(survivors) == 0:
    print("Reason: All survivors starved to death.")
elif choice == "3" and not successful_escape:
    print("Reason: Unsuccessful abandonment. Your team was caught in the open during a horde due to an poorly timed exit.")
else:
    print("Reason: You successfully abandoned the base and escaped at the perfect moment!")


print(f"You survived {days} days.")
