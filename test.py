import json
import urllib.parse
import webbrowser
import PySimpleGUI as sg
from PyPDF2 import PdfReader

# Define the theme
#sg.theme('DarkPurple3')

# Define the layout
layout = [
    [sg.Image('image.png', size=(500,500))],
    [sg.Text('Hack the Job', font=("Helvetica", 24))],
    [sg.Text('Enter your location:'), sg.InputText(key='location')],
    [sg.Text('Enter your desired job:'), sg.InputText(key='job')],
    [sg.Text('Upload your resume (PDF only):')],
    [sg.InputText(key='resume_path'), sg.FileBrowse(file_types=(("PDF files", "*.pdf"),))],
    [sg.Button('Submit')],
    [sg.Text('', size=(50, 10), key='result')],
    [sg.Text('', key='message')]
]

# Create the window
window = sg.Window('Location Menu', layout, element_justification='c').Finalize()
window.Maximize()

# Define a function to get the user's location and resume
def get_location_and_resume():
    location = values['location']
    resume_path = values['resume_path']

    # Check if a resume path has been provided
    if resume_path == "":
        window['message'].update('Please upload a resume before submitting', text_color='red')
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
            search_url = "https://www.indeed.ca/jobs?q=" + urllib.parse.quote_plus(" OR ".join(matched_jobs)) + "&l=" + urllib.parse.quote_plus(location)

            # Display the matching jobs and the search URL as a clickable link
            window['result'].update('Matching jobs:\n{}\n\nSearch on Indeed.com:'.format('\n'.join(matched_jobs)))
            window['result'].metadata = search_url
        else:
            window['result'].update('No matching jobs found.')

    # Clear the input fields
    window['location'].update('')
    window['job'].update('')
    window['resume_path'].update('')

    # Show a message
    window['message'].update('Information submitted successfully', text_color='green')

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        get_location_and_resume()
        resume_path = values['resume_path']
        if resume_path.endswith('.pdf'):
            window['resume_path'].update(resume_path)  # Update the resume_path Text element
            # Update the file_path element to display the selected file path
            window['file_path'].update('Selected file: ' + resume_path)
        else:
            sg.popup('Please select a PDF file.')

# Close the window
window.close()
