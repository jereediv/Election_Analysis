   # First we'll import the os module
   # This will allow us to create file paths across operating systems
import os
   # Module for reading CSV files
import csv

# Create a filename variable to a direct or indirect path
csvpath = "election_results.csv"

# Create a filename variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

with open(csvpath) as csvfile:
    print(csvfile)
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(csvreader)
    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")   
    # Read each row of the data after the header

# Import the datetime class from the datetime module
import datetime as dt
   # Use the now() attribute on the datetime class to get the time
now = dt.datetime.now()
# Print the present time
print("The time right now is ", now)

   # Read and analize data 
   # Open the election results and read the file
with open(csvpath) as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   # Print each row in the CSV file  
   for row in file_reader:
      # 2. Add the total vote count.
      total_votes += 1      
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
      
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
   election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
   print(election_results, end='')
      # Save the final vote count to the text file.
   txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate liast  
   for candidate_name in candidate_votes:
      # Retrieve vote count of a candidate
      votes = candidate_votes[candidate_name]
      # Calculate the percentage of votes
      vote_percentage = float(votes) / float(total_votes) * 100    
   # TO DO: Print out each candidate's name, vote count and percentage of votes to terminal.
   #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
   # Print each candidate, their voter count, and percentage to the terminal
      candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      print(candidate_results)
      # Save the candidate results to our text file.
      txt_file.write(candidate_results)
      # Determine if the votes are greater than the winning count (Module 3.5.5)
      if (votes > winning_count) and (vote_percentage > winning_percentage):
      # If true then set winning_count = votes and winning_percent = vote_percentage
      # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
      # And set the winning_candidate equal to the cadidate's name.
         winning_candidate = candidate_name
   # Print out the winning candidate, vote count and percentage to terminal
   winning_candidate_summary = (
      f"------------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_percentage:.1f}%\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"------------------------------\n")
   print(winning_candidate_summary)
   # Save the winning candidate's name to the text file.
   txt_file.write(winning_candidate_summary)