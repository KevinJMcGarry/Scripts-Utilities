"""
https://craigdanielmiller.com/2016/09/10/finding-words-with-pypdf2/

This is a script for finding all instances of a given search word (or multiple search words) in a PDF.

For our example, we’ll be using a PDF of Romeo and Juliet.  In this case, our search terms are “Romeo” and “Juliet” (search is not case-sensitive).

"""

import PyPDF2
import re
 
pdfFileObj=open(r'C:\Users\Craig\RomeoAndJuliet.pdf',mode='rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
number_of_pages=pdfReader.numPages
 
pages_text=[]
words_start_pos={}
words={}
 
searchwords=['romeo','juliet']
 
with open('FoundWordsList.csv', 'w') as f:
    f.write('{0},{1}\n'.format("Sheet Number", "Search Word"))
    for word in searchwords:
        for page in range(number_of_pages):
            print(page)
            pages_text.append(pdfReader.getPage(page).extractText())
            words_start_pos[page]=[dwg.start() for dwg in re.finditer(word, pages_text[page].lower())]
            words[page]=[pages_text[page][value:value+len(word)] for value in words_start_pos[page]]
        for page in words:
            for i in range(0,len(words[page])):
               if str(words[page][i]) != 'nan':
                    f.write('{0},{1}\n'.format(page+1, words[page][i]))
                    print(page, words[page][i])
