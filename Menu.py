import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Location Menu")

# Define a function to get the user's location
def get_location():
    location = entry.get()
    print("User location:", location)

# Create a label and entry field for the user's location
label = tk.Label(window, text="Enter your location:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the user's location
button = tk.Button(window, text="Submit", command=get_location)
button.pack()

# Run the main event loop
window.mainloop()
