import PyPDF2
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit

def wordCounter(pdf, pageStart, pageEnd):
    """
    Description
    -----------
    wordCounter() counts the number of words in a given pdf between a given interval of

    Parameters
    ----------
    pdf : string
       Path to the PDF in question
    pageStart : int
        Starting page number
    pageEnd : int
        Ending page number

    Returns
    -------
    wordCount : int
        Total number of words in the interval [pageStart, pageEnd]
    """
    pdf = PyPDF2.PdfReader(pdf)

    # Declare start and end pages, and initialize the word count varialbe
    wordCount = 0 

    for i in range(pageStart-1, pageEnd-1): # Throw on the -1 on pageStart and pageEnd since indexing begins at 0. So page 10 would really be page 9 in the eyes of the program
        content = pdf.pages[i].extract_text() 
        wordCount += len(content.split()) 

    # The counting function counts page numbers, this removes that redundancy by subtracting off the number of pages from the final word count
    wordCount -= len(range(pageStart,pageEnd))
    return(wordCount)

# Initialize the application and the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("PDF Word Counter")
window.setGeometry(700, 400, 500, 300)

# Create the rest of the application
layout=QGridLayout()
# layout.addWidget(QLabel("Starting Page"), 0,0)
layout.addWidget(QLineEdit('Default Value', self),0,0)

# helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
# helloMsg.move(60, 15)
window.show()
sys.exit(app.exec())