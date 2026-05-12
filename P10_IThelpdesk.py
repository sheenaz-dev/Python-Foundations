# --- THE TICKET ENGINE ---
def submit_ticket():
    print("\n--- NEW TICKET ---")
    name = input("Your Name: ")
    issue = input("What is the problem? ")
    
    # 'a' (Append) adds the new ticket to the end of the file
    with open("support_log.txt", "a") as file:
        file.write(f"NAME: {name} | ISSUE: {issue}\n")
    print("✅ Ticket submitted successfully!")

def view_tickets():
    print("\n--- OPEN TICKETS ---")
    try:
        # 'r' (Read) opens the file to view the contents
        with open("support_log.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No tickets found yet.")

# --- THE MAIN LOOP ---
while True:
    choice = input("\n[1] New Ticket [2] View Tickets [3] Quit: ")
    if choice == "1":
        submit_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        break