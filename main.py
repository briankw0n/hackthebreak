import json
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog
import urllib.parse
import webbrowser
from tkinter import *
from PIL import Image, ImageTk
import random
import whyyoudothisjayden
import FederalScrape
import ParseFunction

# Create the main window
window = tk.Tk()
window.title("Location Menu")
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (window_width, window_height))

window.configure(bg="#90A8EE")

# Add the raindrop canvas to the window
raindrop_canvas = tk.Canvas(window, width=window_width, height=window_height, highlightthickness=0, bg="#90A8EE", bd=0, highlightbackground='black')
raindrop_canvas.pack(fill='both', expand=True)
raindrop_canvas.configure(highlightthickness=0)
raindrop_canvas.configure(bg="#90A8EE")
raindrop_canvas.place(x=0, y=0)

# Draw white raindrop circles on the canvas
for i in range(50):
    x = random.randint(0, window_width)
    y = random.randint(0, window_height)
    radius = random.randint(5, 10)
    raindrop_canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white", outline="white")

# Configure the font and colors
font = ("Helvetica", 12)
label_color = "#5D3FD3"
button_color = "#800080"

def open_link(url):
    webbrowser.open_new_tab(url)

# Define a function to get the user's location and resume
def get_location_and_resume():
    location = location_entry.get()
    resume_path = resume_path_label.cget("text")

    # Check if a resume path has been provided
    if resume_path == "":
        message_label.config(text="Please upload a resume before submitting", fg="red")
        return

    # Open the PDF file in read-binary mode
    with open(resume_path, 'rb') as pdf_file:
        # Create a PdfReader object to read the PDF
        pdf_reader = PdfReader(pdf_file)

        # Extract text from each page of the PDF and store in a list
        text_pages = []
        for page_num in range(len(pdf_reader.pages)):
            text_pages.append(pdf_reader.pages[page_num].extract_text())

        # Load the job titles from a JSON file
        with open('jobs.json', 'r') as f:
            job_titles = json.load(f)

        # Loop through each job title in the list and check for matches in the extracted text
        matched_jobs = []
        for job_title in job_titles["jobs"]:
            for text in text_pages:
                if job_title.lower() in text.lower():
                    matched_jobs.append(job_title)

        # Remove duplicates from matched_jobs list
        matched_jobs = list(set(matched_jobs))

        if matched_jobs:
            # Generate the search URL for Indeed.com
            search_url = "https://www.bcjobs.ca/search-jobs?q=" + urllib.parse.quote_plus(
                " ".join(matched_jobs)) + "&location=" + urllib.parse.quote_plus(location)
            result_label.config(text="Matching jobs for {}".format(", ".join(matched_jobs)) + ":\n")
            job_list = whyyoudothisjayden.get_job_description(search_url)
            job_details = ""
            for i, job in enumerate(job_list):
                if i >= 3:
                    break
                title = job['title']
                company = job['company']
                link = "https://www.bcjobs.ca" + job['link']
                #webbrowser.open_new_tab(link)
                job_details += f"Title: {title}\nCompany: {company}\nLink: {link}\n\n"
            result_label.config(text=result_label.cget("text") + "\n" + job_details)

            search_url2 = "https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=" + urllib.parse.quote_plus(
                " ".join(matched_jobs)) + "&location=" + urllib.parse.quote_plus(location)
            result_label2.config(text="Matching jobs for {}".format(", ".join(matched_jobs)) + ":\n")
            job_list2 = FederalScrape.get_jobDescription(search_url2)
            job_details2 = ""
            for j, job2 in enumerate(job_list2):
                if j >= 3:
                    break
                title2 = job2['title']
                company2 = job2['company']
                link2 = "https://www.jobbank.gc.ca" + job2['link']
                #webbrowser.open_new_tab(link2)
                job_details2 += f"Title: {title2}\nCompany: {company2}\nLink: {link2}\n\n"
            result_label2.config(text=result_label2.cget("text") + "\n" + job_details2)

            # Destroy any previous link widget
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") == "blue":
                    widget.destroy()

            #link = tk.Label(window, text=search_url, fg="blue", cursor="hand2")
            #link.pack()
            #link.bind("<Button-1>", lambda event: webbrowser.open(search_url))
            #comment
        else:

            result_label.config(text="No matching jobs found.")
            # Destroy any previous link widget
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and widget.cget("fg") == "blue":
                    widget.destroy()

        # Clear the input fields
        location_entry.delete(0, tk.END)
        resume_path_label.config(text="")

        # Show a message
        message_label.config(text="Information submitted successfully", fg="green")

# Create a label for the title text
title_label = tk.Label(window, text="Hack the Job", font=("Helvetica", 35), fg="#5D3FD3", bg="#90A8EE", pady=10)
title_label.pack()

# Create a label and entry field for the user's location
location_label = tk.Label(window, text="Enter your location:", font=font, fg=label_color, bg="#90A8EE")
location_label.pack(pady=10)
location_entry = tk.Entry(window, font=font)
location_entry.pack(padx=10, pady=5)

# Create a label and button for the user's resume
resume_label = tk.Label(window, text="Upload your resume (PDF only):", font=font, fg=label_color, bg="#90A8EE")
resume_label.pack(pady=10)
resume_path_label = tk.Label(window, font=font, fg=label_color, bg="#90A8EE")
resume_path_label.pack(padx=10, pady=5)

# Create a button to upload the user's resume
def browse_resume():
    resume_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    resume_path_label.config(text=resume_path)
resume_button = tk.Button(window, text="Browse", font=font, bg=button_color, fg="white", command=browse_resume)
resume_button.pack()
resume_button.place(relx=0.45, rely=0.331, anchor="center")

# Create a button to submit the user's location and resume
submit_button = tk.Button(window, text="Submit", font=font, bg=button_color, fg="white", command=get_location_and_resume)
submit_button.pack()
submit_button.place(relx=0.55, rely=0.331, anchor="center")

# Create a label for the result
result_label = tk.Label(window, text="", font=font, fg=label_color, bg="#90A8EE")
result_label.pack(side="left", pady=10)

result_label2 = tk.Label(window, text="", font=font, fg=label_color, bg="#90A8EE")
result_label2.pack(side="right", pady=10)

# Create a label for messages
message_label = tk.Label(window, font=font, fg="red", bg="#90A8EE")
message_label.pack()

# Run the main event loop
window.mainloop()