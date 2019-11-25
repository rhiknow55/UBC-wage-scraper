import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords # Words such as "a", "the"

text = ""
keywords = []

def parse_text():
    filename = "FY19_Financial_Information_Act_Report.pdf"

    # open() allows you to read the file
    pdfFileObj = open(filename,'rb') # rb = read binary

    # The pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # discerning the number of pages will allow us to parse through all the pages
    numPages = 104 # The end of wages
    count = 41
    global text

    while count < numPages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    # This if statement exists to check if the above library returned words.
    # It's done because PyPDF2 cannot read scanned files.
    # If the above returns as False, we run the OCR library
    # textract to #convert scanned/image based PDF files into text

    if text != "":
        text = text
    else:
        text = textract.process(filename, method="tesseract", language="eng")

    # Now we have a text variable which contains all the text derived
    # from our PDF file. Type print(text) to see what it contains. It
    # likely contains a lot of spaces, possibly junk such as '\n' etc.

    # If you print, it'll privt 131 pages worth of words. you will regret

def get_words():
    # The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)

    # we'll create a new list which contains punctuation we wish to clean
    punctuations = ['']

    # We initialize the stopwords variable which is a list of words like
    # "The", "I", "and", etc. that don't hold much value as keywords
    stop_words = stopwords.words("english")

    # We create a list comprehension which only returns a list of words
    # that are NOT IN stop_words and NOT IN punctuations.
    global keywords
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

parse_text()
get_words()
