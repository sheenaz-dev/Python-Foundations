# --- This mini project explain If/Else Logic

# --- STEP 1: Assign Password to the variable
secret_password = "pythonISA"

# --- STEP 2: USER INPUT
print("Welcome to the Secure Vault.") 

guess = input("Enter the secret password: ") 

# --- STEP 3: THE DECISION --- 

if guess == secret_password:
    print("ACCESS GRANTED!") 

    print("Welcome! Your mission is to master Python") 
else:
    print("ACCESS DENIED!") 

    print("Security has been alerted. Please try again.") 

