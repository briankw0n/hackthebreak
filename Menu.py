import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Location Menu")
window.geometry("1000x500")

# Define a function to get the user's location
def get_location():
    location = entry.get()
    print("User location:", location)

# Configure the font and colors
font = ("Helvetica", 14)
label_color = "#444444"
button_color = "#3366CC"

# Create a label and entry field for the user's location
label = tk.Label(window, text="Enter your location:", font=font, fg=label_color)
label.pack(pady=10)
entry = tk.Entry(window, font=font)
entry.pack(padx=10, pady=10)

# Create a button to submit the user's location
button = tk.Button(window, text="Submit", font=font, bg=button_color, fg="white", command=get_location)
button.pack(pady=10)

# Run the main event loop
window.mainloop()
