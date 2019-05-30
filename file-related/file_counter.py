import os
import time
import shutil
import openpyxl
import image  # pip3 install image. needed for xlsx processing
from PyPDF2 import PdfFileReader # be sure to 'pip3 install PyPDF2'


root_dir = '/Users/kevinmcgarry/Clients/ABB/National Grid'
final_report_dest = '/Users/kevinmcgarry/Clients/report.txt'
word_directory = '/Users/kevinmcgarry/Clients/ABB/msg_docs'
file_extension_list = []
file_extension_count = {}


def generate_file_extension_list(root_dir):
    with open(final_report_dest, 'w') as report:
        for current_dir, subdirs, files in os.walk(root_dir):
            for each_file in files:
                full_path = os.path.join(current_dir, each_file)
                file_name, file_extension = os.path.splitext(full_path)
                if each_file.endswith("DS_Store"):
                    continue
                if file_extension not in file_extension_list:
                    file_extension_list.append(file_extension)
    list_sorted = sorted(file_extension_list)
    # print(list_sorted)
    return list_sorted


def generate_file_extension_count(root_dir):
    with open(final_report_dest, 'w') as report:
        for current_dir, subdirs, files in os.walk(root_dir):
            for each_file in files:
                full_path = os.path.join(current_dir, each_file)
                file_name, file_extension = os.path.splitext(full_path)
                if file_extension not in file_extension_count:
                    file_extension_count[file_extension] = 1
                else:
                    file_extension_count[file_extension] += 1
    print(file_extension_count)
    new_count_list = []
    for k,v in file_extension_count.items():
        new_count_list.append((v, k))
    new_count_list_sorted = sorted(new_count_list, reverse=True)
    print(new_count_list_sorted)


def sum_files_by_ext(root_dir):

    a = generate_file_extension_list(root_dir)
    print(a)
    # time.sleep(10)

    for extension in a:
        ext_count = 0
        ext_sum = 0
        for current_dir, subdirs, files in os.walk(root_dir):
            for each_file in files:
                if each_file.endswith("DS_Store"):
                    continue
                full_path = os.path.join(current_dir, each_file)
                file_name, file_extension = os.path.splitext(full_path)
                if extension == file_extension:
                    ext_count += 1
                    ext_sum += os.path.getsize(full_path)
        print(f"There are {ext_count} files with extension {extension} for a total of {ext_sum} bytes")


def count_pdf_pages(root_dir):
    num = 0
    for current_dir, subdirs, files in os.walk(root_dir):
        for each_file in files:
            try:
                full_file_path = os.path.join(current_dir, each_file)
                # print(f"Pre-PDF File ---- {full_file_path}")
                if full_file_path.lower().endswith("pdf"):
                    # print(full_file_path)
                    pdf = PdfFileReader(open(full_file_path, 'rb'))
                    num += pdf.getNumPages()
                    # time.sleep(1)
            except:
                print(full_file_path)
    print(f"There are a total of {num} pdf pages")


def copy_word_docs(root_dir):
    with open(final_report_dest, 'w') as report:
        for current_dir, subdirs, files in os.walk(root_dir):
            for each_file in files:
                full_path = os.path.join(current_dir, each_file)
                local_path = os.path.dirname(full_path)
                # print(local_path)
                file_name, file_extension = os.path.splitext(full_path)
                if full_path.endswith('.msg'):
                    shutil.copy(full_path, word_directory)


def excel_sheet_count(root_dir):
    sheet_count = 0
    for current_dir, subdirs, files in os.walk(root_dir):
        for each_file in files:
            full_path = os.path.join(current_dir, each_file)
            file_name, file_extension = os.path.splitext(full_path)
            if full_path.endswith('.xlsx'):
                print(f"Opening Excel Document {full_path}")
                try:
                    wb = openpyxl.load_workbook(full_path)
                    res = len(wb.sheetnames)
                    sheet_count += res
                except ModuleNotFoundError:
                    print("No Module Named PIL")
    print(sheet_count)


if __name__ == "__main__":
    # copy_word_docs(root_dir)
    # sum_files_by_ext('/Users/kevinmcgarry/Clients/ABB')
    # count_pdf_pages('/Users/kevinmcgarry/Clients/ABB/PowerPoint_Output')
    excel_sheet_count(root_dir='/Users/kevinmcgarry/Clients/ABB/Excel_Docs')



# import pandas as pd
# import os
#
#
# from PyPDF2 import PdfFileReader
# df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])
# for root, dirs, files in os.walk(r'/home/benjamin/docs/'):
#     for f in files:
#         if f.endswith(".pdf"):
#             pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
#             df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
#             df = df.append(df2, ignore_index=True)
# print(df.head)