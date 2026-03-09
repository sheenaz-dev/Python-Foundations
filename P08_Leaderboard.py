# --- STEP 1: CAPTURE AND SAVE DATA ---
print("--- ISA TECH LEADERS: LOG NEW SCORE ---")
name = input("Enter Student Name: ")
score = input("Enter Score: ")

# We use 'a' for Append so we don't delete previous students
with open("top_scores.txt", "a") as file:
    # We add \n so the next entry starts on a new line
    file.write(f"{name}, {score}\n")

print(f"✅ Success! {name}'s score has been saved to the disk.\n")

# --- STEP 2: RETRIEVE AND DISPLAY DATA ---
print("--- HALL OF FAME: ALL SAVED SCORES ---")
print("-" * 35)

try:
    with open("top_scores.txt", "r") as file:
        for line in file:
            # Clean the text and split into Name and Score
            clean_line = line.strip()
            student_data = clean_line.split(", ")
            
            print(f"STUDENT: {student_data[0]} | SCORE: {student_data[1]}")
except FileNotFoundError:
    print("No scores found yet. Log a score to create the file!")

print("-" * 35)