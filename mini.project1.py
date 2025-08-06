import tkinter as tk
from tkinter import messagebox

players = ["Rohit", "Virat", "Gill", "Surya"]
player_stats = {}

# GUI window
root = tk.Tk()
root.title("Cricket Player Stats")
root.geometry("400x500")
root.config(bg="lightyellow")

entry_widgets = {}

# Heading
tk.Label(root, text="Enter Runs for 3 Matches", font=("Arial", 14, "bold"), bg="lightyellow").pack(pady=10)

# Input fields
for player in players:
    frame = tk.Frame(root, bg="lightyellow")
    frame.pack(pady=5)
    tk.Label(frame, text=player, font=("Arial", 12), width=6, bg="lightyellow").pack(side=tk.LEFT)
    entries = []
    for i in range(3):
        e = tk.Entry(frame, width=5)
        e.pack(side=tk.LEFT, padx=2)
        entries.append(e)
    entry_widgets[player] = entries

# Function to process data
def calculate_stats():
    result_text.delete("1.0", tk.END)
    player_stats.clear()

    for player in players:
        match_runs = []
        i = 0
        while i < 3:
            val = entry_widgets[player][i].get()
            if val.isdigit():
                match_runs.append(int(val))
                i += 1
            else:
                messagebox.showerror("Invalid Input", f"Enter valid number for {player} - Match {i+1}")
                return
        player_stats[player] = match_runs

    # Display Stats
    result_text.insert(tk.END, "--- Player Stats ---\n")
    for player in players:
        runs = player_stats[player]
        total = sum(runs)
        avg = total / 3
        result_text.insert(tk.END, f"{player}: Runs = {runs}, Total = {total}, Avg = {avg:.2f}\n")

    result_text.insert(tk.END, "\n--- Run Visualization (1★ = 10 runs) ---\n")
    for player in players:
        total = sum(player_stats[player])
        stars = total // 10
        result_text.insert(tk.END, f"{player:6}: {'★' * stars}\n")

# Button to calculate
tk.Button(root, text="Calculate Stats", command=calculate_stats, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

# Output Text Area
result_text = tk.Text(root, height=15, width=40, font=("Courier", 10))
result_text.pack(pady=10)

root.mainloop()
