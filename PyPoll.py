   # First we'll import the os module
   # This will allow us to create file paths across operating systems
import os
   # Module for reading CSV files
import csv

# Create a filename variable to a direct or indirect path
csvpath = "election_results.csv"

#csvpath = "..\Class Folder\Election_Analysis\election_results.csv"
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

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
   # Open the election results and read the file
with open(csvpath) as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   # Print each row in the CSV file  
   for row in file_reader:
      # 2. Add the total vote count.
      total_votes += 1
   # 3. Print the total votes.
      #print(total_votes)
# Print the candidate name from each row
      candidate_name = row[2]
# If the candidate does not match an existing candidate..            
      if candidate_name not in candidate_options:
         # Add the candidate name to the candidate list
         candidate_options.append(candidate_name)
         # Begin tracking that candidate's vote count
         candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate liast
for candidate_name in candidate_votes:
   # Retrieve vote count of a candidate
   votes = candidate_votes[candidate_name]
   # Calculate the percentage of votes
   vote_percentage = float(votes) / float(total_votes) * 100
   # Print the candidate name and percentage of votes
   print(f"{candidate_name}: received {vote_percentage}% of votes.")
print(candidate_votes)





































