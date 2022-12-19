import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Command Line Interface")
root.geometry("800x600")

# Create a text entry box for the user to enter commands
entry = tk.Entry(root)
entry.pack(side="bottom",fill="x")

# Create a function to be called when the user hits the Enter key
def on_enter(event):
    # Get the command from the text entry box
    command = entry.get()
    # Clear the text entry box
    entry.delete(0, 'end')
    # Print the command to the console
    print(f"You entered: {command}")

def print_on_screen(event):
    command = entry.get()
    entry.delete(0,'end')
    label = tk.Label(root, text=command, wraplength="800", justify="left")
    label.pack(anchor="w", after=entry, side="bottom")

# Bind the Enter key to the on_enter function
entry.bind("<Return>", print_on_screen)

# Run the tkinter event loop
root.mainloop()
