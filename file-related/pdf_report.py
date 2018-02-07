"""
utility to recursively search all folders for pdf files, pull relevant information from each file
and create a tab delimited file from the results

to do's --
1) add logic/exception handling for encountering non-pdf files
2) add more detailed comments
3) generify variables
4) move this into a function and perhaps merge this with the pdf indexer script. user response determines if indexing and/or pdf_reporter functions used

***** Requirements ****
pip3 install pypdf2 (don't use original pypdf with python 3.x+)

"""

import PyPDF2  # https://github.com/mstamy2/PyPDF2
import os


tart_dir = "/Users/kevinmcgarry/temp24/"  # to be set as an argument
file_path_dest = "/Users/kevinmcgarry/temp22/info.txt"  # to be set as an argument

with open(file_path_dest, 'w') as outputfile:
    outputfile.write("File Name\t Pages\t Creation Date\t Modified Date\n")  # column headers
    for current_dir, subdirs, files in os.walk(start_dir):
        # print(files)
        for each_file in files:
            full_path = os.path.join(current_dir, each_file)
            relative_path = full_path[len(start_dir):]  # stripping off user path information
            if full_path.endswith("DS_Store"):
                continue
            print(relative_path)
            # print(full_path)
            reader = PyPDF2.PdfFileReader(open(full_path, 'rb'))
            doc_info = reader.getDocumentInfo()
            num_pages = reader.getNumPages()
            creation_date = doc_info['/CreationDate'][2:10]
            modified_date = doc_info['/ModDate'][2:10]
            # substitute full_path in the f string first position for entire path
            full_doc_info = f"{relative_path} \t {num_pages} \t {creation_date} \t {modified_date} \n"
            outputfile.write(full_doc_info)

# The PDF-izer
# would you like to index all pdfs found? y or n
# would you like to print a report, y or no
# starting dir location
# where to store report file
