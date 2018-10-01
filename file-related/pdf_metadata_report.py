"""
utility to recursively search all folders for pdf files, pull relevant information from each file
and create a tab delimited file from the results

to do's --
1) update first argument to throw a detailed error with example if path isn't specified

# The PDF-izer
# would you like to index all pdfs found? y or n
# would you like to print a report, y or no
# starting dir location
# where to store report file


***** Requirements ****
pip3 install pypdf2 (don't use original pypdf with python 3.x+)

"""


#! /usr/local/bin/python3

import PyPDF2  # https://github.com/mstamy2/PyPDF2
# more PyPDF2 documentation - http://pythonhosted.org/PyPDF2/PdfFileReader.html
import os
import sys


if len(sys.argv) > 1:  # first argument specifies directory to start the operation on
    target_dir = sys.argv[1]
else:
    target_dir = '.'  # default directory to use if one isn't specified at runtime

if len(sys.argv) > 2:  # second argument is location to store the report
    final_report_dest = sys.argv[2]
else:
    final_report_dest = './report.txt'  # default directory to use if one isn't specified at runtime


def pdf_reporter(target_dir, final_report_dest):
    with open(final_report_dest, 'w') as outputfile:
        outputfile.write("File Name\t Pages\t Creation Date\t Modified Date\n")  # column headers
        for current_dir, subdirs, files in os.walk(target_dir):
            # print(files)
            for each_file in files:
                full_path = os.path.join(current_dir, each_file)
                relative_path = full_path[len(target_dir):]  # stripping off user path information
                if not full_path.endswith("pdf"):  # only operate on pdf files
                    continue
                reader = PyPDF2.PdfFileReader(open(full_path, 'rb'))
                if reader.isEncrypted is True:  # skip encrypted files
                    print(f"{full_path} is encrypted and is being skipped")
                    continue
                doc_info = reader.getDocumentInfo()
                num_pages = reader.getNumPages()
                # using slicing to pull out exact date from string (eg '/ModDate': "D:20121030173901-04'00'")
                try:
                    creation_date = doc_info['/CreationDate'][2:10]
                except KeyError:
                    creation_date = "n/a"
                try:
                    modified_date = doc_info['/ModDate'][2:10]
                except KeyError:
                    modified_date = "n/a"
                # substitute full_path in the f string first curly-brace position for entire path
                full_doc_info = f"{relative_path} \t {num_pages} \t {creation_date} \t {modified_date} \n"
                outputfile.write(full_doc_info)


if __name__ == '__main__':
    pdf_reporter(target_dir, final_report_dest)
