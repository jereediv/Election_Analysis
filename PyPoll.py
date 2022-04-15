   # First we'll import the os module
   # This will allow us to create file paths across operating systems
import os
   # Module for reading CSV files
import csv

csvpath = os.path.join('..', 'resources', 'election_results.csv')
   #csvpath = "../resources/election_results.csv"

   # # Method 1: Plain Reading of CSV files

with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))

   # Method 2: Improved Reading using CSV module

#with open(csvpath) as csvfile:
#    print(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
#    csvreader = csv.reader(csvfile, delimiter=",")
    #  print(csvreader)
    # Read the header row first (skip this step if there is no header)
#    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    # Read each row of the data after the header
#    for row in csvreader:
#        first_name = row[0]
#        last_name = row[1]
#        print(f'{first_name} {last_name}')




































