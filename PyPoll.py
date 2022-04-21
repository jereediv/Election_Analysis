   # First we'll import the os module
   # This will allow us to create file paths across operating systems
import os
   # Module for reading CSV files
import csv

csvpath = ("election_results.csv")
#csvpath = "..\Class Folder\Election_Analysis\election_results.csv"
# Create a filename variable to a direct or indirect path

#csvpath = os.path.join("analysis", "election_analysis.txt")

with open(csvpath) as csvfile:
    print(csvfile)
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(csvreader)
    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of the data after the header
    #for row in csvreader:
        #print(row)
   
# Import the datetime class from the datetime module

import datetime as dt
   # Use the now() attribute on the datetime class to get the time
now = dt.datetime.now()
# Print the present time
print("The time right now is ", now)

# Create a filename variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:
# Write some data to the file
   #txt_file.write("Hello World")
# Write three counties to the file
   txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
   # Read and analize data
   









































