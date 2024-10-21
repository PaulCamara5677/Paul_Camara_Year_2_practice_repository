import tkinter as tk

def create_button(label):
    button = tk.Button(root, text=label, font=("Arial", 24), command=lambda: None)
    button.pack(expand=True, fill=tk.BOTH)

# Creates the main window
root = tk.Tk()
root.title("Buttons A, B, C, D")

# Sets the window to device's/window's fullscreen
root.attributes("-fullscreen", True)

# Creates the four buttons
create_button("A")
create_button("B")
create_button("C")
create_button("D")

# Runs the application
root.mainloop()