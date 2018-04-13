# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 19:05:37 2018

@author: giovanimachado

Based on asweigart code (automatetheboringstuff.com)
"""

import PyPDF2, os
import re

def sorted_nicely( l ):
    """ Sorts the given iterable in the way that is expected (eg.: 11 after 2).
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)


# Get all the PDF filenames.
# The os.listdir('.') call will return a list of every file in the current working directory
pdfFiles = []
print('Enter the path where are the files:' )
path = input('prompt: ')
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        filename=path+filename
        pdfFiles.append(filename)
    #print(filename)
#pdfFiles.sort(key=str.lower)

pdfFiles=sorted_nicely(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    print(filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
   
#For each PDF, the loop opens a filename in read-binary mode by calling open() 
#with 'rb' as the second argument. The open() call returns a File object, which 
#gets passed to PyPDF2.PdfFileReader() to create a PdfFileReader object for that
# PDF file.
    
# Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        
# Save the resulting PDF to a file.
    pdfOutput = open('@Completo.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

#Passing 'wb' to open() opens the output PDF file, allminutes.pdf, in 
#write-binary mode. Then, passing the resulting File object to the write() 
#method creates the actual PDF file. A call to the close() method finishes 
#the program.