# --- STEP 1: DEFINE THE ROOMS (FUNCTIONS) ---

def start_room():
    print("\n--- THE CASTLE GATE ---")
    print("You stand before a massive stone gate. It is locked.")
    choice = input("Do you [1] Search the bushes or [2] Knock on the door? ")
    
    if choice == "1":
        print("You found a rusty key!")
        return "treasure_room" # Moving to the next room
    else:
        print("A guard wakes up and chases you away. Game Over.")
        return "end"

def treasure_room():
    print("\n--- THE GOLDEN VAULT ---")
    print("The rusty key fits! You are surrounded by gold.")
    choice = input("Do you [1] Take the gold or [2] Leave it and explore further? ")
    
    if choice == "1":
        print("The vault was a trap! The doors lock forever. Game Over.")
        return "end"
    else:
        print("You found a secret exit to freedom. YOU WIN!")
        return "end"

# --- STEP 2: THE GAME ENGINE (LOOP) ---

current_room = "start"

print("Welcome to the Python Adventure Engine!")

while current_room != "end":
    if current_room == "start":
        current_room = start_room()
    elif current_room == "treasure_room":
        current_room = treasure_room()

print("\n--- THANKS FOR PLAYING ---")
