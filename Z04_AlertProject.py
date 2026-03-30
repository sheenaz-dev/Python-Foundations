import tkinter as tk
from tkinter import messagebox

def run_scan():
    content = text_area.get("1.0", "end-1c").lower()
    
    # 1. Logic Databases
    safety_triggers = ["suicide", "bomb", "kill", "weapon"]
    tone_triggers = ["hate", "ugly", "stupid", "loser"]
    
    results = []
    status_color = "green"

    # 2. Scanning Logic
    for word in safety_triggers:
        if word in content:
            results.append(f"🚨 SAFETY ALERT: Found '{word}'")
            status_color = "red"
            
    for word in tone_triggers:
        if word in content:
            results.append(f"⚠️ TONE ALERT: Found '{word}'")
            if status_color != "red": status_color = "orange"

    # 3. UI Update
    if not results:
        result_label.config(text="✅ SCAN CLEAR: No issues found.", fg="green")
    else:
        result_label.config(text="\n".join(results), fg=status_color)

# --- UI Setup ---
root = tk.Tk()
root.title("ISA Safety Hub v1.0")
root.geometry("500x400")
root.configure(bg="#f8fafc")

tk.Label(root, text="ISA CONTENT SCANNER", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#1e293b").pack(pady=10)
tk.Label(root, text="Paste text below to check for Safety & Tone:", bg="#f8fafc").pack()

text_area = tk.Text(root, height=8, width=50, font=("Arial", 10))
text_area.pack(pady=10)

scan_btn = tk.Button(root, text="START SCAN", command=run_scan, bg="#38bdf8", fg="white", font=("Arial", 10, "bold"), width=20)
scan_btn.pack(pady=10)

result_label = tk.Label(root, text="System Ready...", font=("Arial", 10, "italic"), bg="#f8fafc")
result_label.pack(pady=20)

root.mainloop()