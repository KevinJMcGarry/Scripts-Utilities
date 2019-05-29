'''
script used for removing the header line (line 1) from all csv files.

things to note --
each row in a csv file object (created via csv.reader()) is a list of each separated item. Because of this you can't do the standard output.write(line) method as you'll get an
error about trying to write a list for each row - you can only write strings with this method. This is why you need to use the writerow(row) method. This writes each row/list 
as a string in the outputfile.

so three methods we will use to write the csv lines to a new file (to remove the header line) --
1. csv.reader = allows you to read a csv file row by row (each row as a list) into a csv object variable
2. csv.writer = creates another csv object, this time an empty one that will be used with teh writerow method to write each row of data (as a string)
3. csv.writerow = writes each row/list of csv data into a file. each row written as a string, each string separated by a newline

good test site containing various csv files - https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
'''

import os
import csv

original_csv_folder = input('please enter the full path the folder containing the original csv file(s): ')
updated_csv_folder = input('please enter the full path the folder containing the updated (header line removed) csv file(s): ')

# check to see if updated_csv_folder hasn't already been created and if not, create it
if not os.path.exists(updated_csv_folder):
    os.mkdir(updated_csv_folder)


for file in os.listdir(original_csv_folder):
    if file.endswith('.csv'):
        full_path_original_file = os.path.join(original_csv_folder, file)
        full_path_updated_file = os.path.join(updated_csv_folder, file)
        with open(full_path_original_file, 'r') as inputfile:
            with open(full_path_updated_file, 'w') as outputfile:
                csvFileInputObject = csv.reader(inputfile)  # creates a csv object that contains a list for each row of csv data
                csvFileOutputObject = csv.writer(outputfile)  # creates a csv object to be written to 
                for row in csvFileInputObject:
                    if csvFileInputObject.line_num == 1:  # skip writing the first line/list in the csv file
                        continue
                    csvFileOutputObject.writerow(row)
