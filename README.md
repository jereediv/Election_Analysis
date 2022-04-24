# Election Analysis

## Project Overview
A Colorado Board of Elections employee has aked for an election audit of a recent local congressional election. We want to break the data down into votes per county and each county's share of the total votes cast. There are 5 goals for this project listed below.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Summary of results
- Total votes cast :  369,711
- Count and percentage of total votes for each county in the precint
  - Jefferson : 38,855 votes (10.5% of total votes)
  - Denver : 306,055 votes (82.8% of total votes)
  - Arapahoe : 24,801 votes (6.7% of total votes)
- Candidates
  - Charles Casper Stockham : 85,213 votes (23%)
  - Diana DeGette : 272,892 votes (73.8%)
  - Raymon Anthony Doane : 11,606 votes (3.1%)
- Denver county had the largest turnout
- Dian DeGette won the election with 73.8% of the vote (272,892 votes)

The script used to generate these results can be used with little modifications for any election. We can use this script to compare the candidates' margins, individually in each county. We can also use it to judge how turnout correlates to candidate advantage.

##Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.66.2
