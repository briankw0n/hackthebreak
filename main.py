import json
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

# Define dictionary of job titles
job_titles = {
  "jobs": [
    "Software Developer",
    "Data Scientist",
    "Systems Administrator",
    "Cybersecurity Analyst",
    "Web Developer",
    "Database Administrator",
    "Artificial Intelligence Engineer",
    "Cloud Architect",
    "Network Administrator",
    "Full Stack Developer",
    "UI/UX Designer",
    "DevOps Engineer",
    "IT Project Manager",
    "Machine Learning Engineer",
    "Front-end Developer",
    "Back-end Developer",
    "Mobile Application Developer",
    "Business Intelligence Analyst",
    "Game Developer",
    "Quality Assurance Engineer"
  ]
}

# Create the main window
window = tk.Tk()
window.title("Location Menu")
window.geometry("300x200")
window.configure(bg="black")

# Define a function to get the user's location and resume
def get_location_and_resume():
    location = location_entry.get()
    resume_path = resume_path_label.cget("text")

    # Open the PDF file in read-binary mode
    with open(resume_path, 'rb') as pdf_file:
        # Create a PdfReader object to read the PDF
        pdf_reader = PdfReader(pdf_file)

        # Extract text from each page of the PDF and store in a list
        text_pages = []
        for page_num in range(len(pdf_reader.pages)):
            text_pages.append(pdf_reader.pages[page_num].extract_text())

        # Loop through each job title in the dictionary and check for matches in the extracted text
        for job_title in job_titles["jobs"]:
            for text in text_pages:
                if job_title.lower() in text.lower():
                    print(f"Matching keyword(s) for {job_title}: {job_title}")

    # Clear the input fields
    location_entry.delete(0, tk.END)
    resume_path_label.config(text="")

    # Show a message
    message_label.config(text="Information submitted successfully", fg="green")

# Configure the font and colors
font = ("Helvetica", 14)
label_color = "white"
button_color = "#800080"

# Create a label for the title text
title_label = tk.Label(window, text="Hack the Job", font=("Helvetica", 24), fg="white", bg="black", pady=10)
title_label.pack()

# Create a label and entry field for the user's location
location_label = tk.Label(window, text="Enter your location:", font=font, fg=label_color, bg="black")
location_label.pack(pady=10)
location_entry = tk.Entry(window, font=font)
location_entry.pack(padx=10, pady=5)

# Create a label and button for the user's resume
resume_label = tk.Label(window, text="Upload your resume (PDF only):", font=font, fg=label_color, bg="black")
resume_label.pack(pady=10)
resume_path_label = tk.Label(window, font=font, fg=label_color, bg="black")
resume_path_label.pack(padx=10, pady=5)

# Create a button to upload the user's resume
def browse_resume():
    resume_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    resume_path_label.config(text=resume_path)
resume_button = tk.Button(window, text="Browse", font=font, bg=button_color, fg="white", command=browse_resume)
resume_button.pack(pady=5)

# Create a button to submit the user's location and resume
submit_button = tk.Button(window, text="Submit", font=font, bg=button_color, fg="white", command=get_location_and_resume)
submit_button.pack(pady=10)

# Create a label for messages
message_label = tk.Label(window, font=font, fg="red", bg="black")
message_label.pack()

# Run the main event loop
window.mainloop()
