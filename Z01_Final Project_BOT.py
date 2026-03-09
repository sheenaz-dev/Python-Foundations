# --- STEP 1: THE KNOWLEDGE BASE ---
# A dictionary where keys are 'keywords' and values are 'solutions'
knowledge_base = {
    "schoology": "Go to isa.schoology.com and use your school email to login.",
    "wifi": "Connect to 'ISA_Student_Guest' and enter the password provided in the lobby.",
    "powerschool": "Check the 'Grades' tab. If it's locked, contact the Data Manager.",
    "printing": "Send your file to print@isa.edu and scan your ID at the library station.",
    "password": "Reset your ISA account at the main office or via the 'Forgot Password' link."
}

# --- STEP 2: THE LOGGING FUNCTION ---
def log_unresolved_issue(user_question):
    """Saves unknown questions to a file for a human Tech Leader to review."""
    with open("pending_requests.txt", "a") as file:
        file.write(f"UNRESOLVED: {user_question}\n")

# --- STEP 3: THE MAIN BOT LOOP ---
print("--- ISA STUDENT TECH LEADERS: VIRTUAL ASSISTANT ---")
print("Type 'exit' to quit. How can I help you today?")

while True:
    user_input = input("\nDescribe your issue: ").lower()
    
    if user_input == "exit":
        print("Goodbye! Reach out to an STL member if you need more help.")
        break
    
    # Check if any keyword from our dictionary is in the user's sentence
    found_answer = False
    for keyword in knowledge_base:
        if keyword in user_input:
            print(f"💡 BOT SUGGESTION: {knowledge_base[keyword]}")
            found_answer = True
            break # Stop looking once we find a match
            
    if not found_answer:
        print("❌ I'm sorry, I don't have the answer to that yet.")
        print("I have logged your question for our Tech Leader team to review.")
        log_unresolved_issue(user_input)