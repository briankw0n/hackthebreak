import PyPDF2
import json

pdfFileObj = open('Assignment2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get total number of pages
num_pages = pdfReader.getNumPages()

# Read each page and search for the keyword
for page in range(num_pages):
    pageObj = pdfReader.getPage(page)
    text = pageObj.extractText()

    # Search for the keyword in the text
    keyword = "example"
    if keyword in text:
        data = {'keyword': keyword}

        # Convert the data into JSON format
        json_data = json.dumps(data)
        print(json_data)

pdfFileObj.close()
