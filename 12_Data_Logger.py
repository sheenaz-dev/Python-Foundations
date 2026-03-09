# --- STEP 1: WRITING (The 'w' Mode) ---
# This creates the file. Warning: 'w' overwrites everything!
with open("attendance.txt", "w") as file:
    file.write("Sheenaz: Present\n")
    file.write("Alex: Present\n")
    file.write("Jordan: Absent\n")

# --- STEP 2: APPENDING (The 'a' Mode) ---
# Use 'a' to add data without deleting the old stuff.
with open("attendance.txt", "a") as file:
    file.write("Maya: Present\n")

# --- STEP 3: READING (The 'r' Mode) ---
print("--- FETCHING DATA FROM DISK ---")
with open("attendance.txt", "r") as file:
    # We can loop through a file just like a list!
    for line in file:
        # .strip() removes the hidden '\n' at the end of lines
        print(line.strip())