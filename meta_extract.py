#!usr/bin/env python
# This program displays metadata from pdf file

from PyPDF2 import PdfFileReader


def main():
    # Enter the location of 'ANONOPS_The_Press_Release.pdf'
    # Download the PDF if you haven't already
    filename = 'books/api-security-action.pdf'

    pdfFile = PdfFileReader(filename, 'rb')
    data = pdfFile.getDocumentInfo()
    print("----Metadata of the file----")
    for metadata in data:
        print(metadata + ":" + data[metadata])

    print(pdfFile.getOutlines())


if __name__ == '__main__':
    main()
