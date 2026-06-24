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


