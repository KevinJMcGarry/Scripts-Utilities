#! /usr/bin/env python3

"""
Run it as a script passing in arguments ---

example to rename pdf files to tif files - ./ext_renamer.py "/Users/userA/some_dir" ".pdf" ".tif"

"""

import os
import argparse

parser = argparse.ArgumentParser(description='Utility rename all files in a directory with a new extension')
parser.add_argument('directory', help='Enter the full path of the directory that you want to change file extensions in')
parser.add_argument('old_ext', help='Enter the name of the file extension you wish to change from')
parser.add_argument('new_ext', help='Enter the name of the file extension you wish to change to')
args = parser.parse_args()


start_folder = args.directory
old_ext = args.old_ext
new_ext = args.new_ext

for i in os.listdir(args.directory):
    full_file = os.path.join(start_folder, i)
    if os.path.isfile(full_file):
        base_file, ext = os.path.splitext(full_file)
        if ext.lower() == ".pdf":
            os.rename(full_file, base_file + new_ext)
