#!/usr/bin/env python3
# Based on code from: https://gist.github.com/jb0hn/760447d7737555793efe48fb4192802c

# Example usage:
#     python3 rotatepdf.py "pdf to rotate.pdf"

import PyPDF2
import sys
import re

if (len(sys.argv) != 2):
    print("This pdf rotater should be called with only one arg, the name of the file")
    exit (1)

# Get the title of the pdf to be roated
pdfName = sys.argv[1]

# If input file has PDF clean.
if (re.search("^.*\\.pdf$",pdfName)):
    # Probably a better way to do this, but 🤷
    pdfName = pdfName[0:pdfName.rfind('.')]

pdfIn = open(f"{pdfName}.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfIn)
pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    page = pdfReader.pages[pageNum]
    page.rotate(-90)
    pdfWriter.add_page(page)

pdfOut = open(f"{pdfName} - Rotated.pdf", 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()
