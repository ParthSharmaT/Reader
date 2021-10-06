import pyttsx3
import PyPDF2

book=open('net-intro.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
start_page = int(input("Enter the starting page number"))
for num in range(start_page, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()