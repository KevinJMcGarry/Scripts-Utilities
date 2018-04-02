'''
Script used to recursively go through a folder and search pdf files for a specific string of interest.
It then outputs the name of the file (including the full path) and the number of times the word was found in the file.
'''


def pdf_word_finder():

    wordOfInterest = input('Enter the case-sensitive string you want to search for: ')
    startDirectory = input('Enter the full path to the root folder that you want to start your search in: ')

    import PyPDF2
    import os

    file_hits_dict = {}
    file_hits_list = []

    for this_dir, dir_names, file_names in os.walk(startDirectory):
        for eachFile in file_names:
            if eachFile.lower().endswith(('.pdf')):
                fpath = os.path.join(this_dir, eachFile)
                with open(fpath, 'rb') as inputfile:
                    count = 0
                    pdfReader = PyPDF2.PdfFileReader(inputfile)
                    number_of_pages = pdfReader.numPages
                    for page in range(number_of_pages):
                        print(page)
                        extracted_text = pdfReader.getPage(page).extractText()
                        words = extracted_text.split()
                        print(words)
                        for word in words:
                            if word == wordOfInterest:
                                count += 1
                if count > 0:
                    file_hits_dict[fpath] = count  # creating a dictionary of files and word count for sorting

    if len(file_hits_dict) > 0:
        for k, v in file_hits_dict.items():
            file_hits_list.append((v, k))
        file_hits_sorted = sorted(file_hits_list, reverse=True)
        print(f"\nFiles containing the word \"{wordOfInterest}\" sorted by number of times the word occurs --")
        for hit in file_hits_sorted:
            print(hit)
    else:
        print(f"no files were found containing the word \"{wordOfInterest}\"")

pdf_word_finder()
