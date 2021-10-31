# The following data is needed: 
# •	Total number of votes cast
# •	A complete list of candidates who received votes
# •	Total number of votes each candidate received
# •	Percentage of votes each candidate won
# •	The winner of the election based on popular vote

#       1. open the .csv file
#       2. count all the records using a for loop (or accumulate total_votes_cast while you are looping through to get the total number of votes for each canditate)
#       3. list all the candidates recieving votes (ever record has a candidate...so, we don't have to check if the candidate received a vote)
#           define LIST candidate_votes we need to have candidate_name and vote_tally.
#           read record
#           does the canditate exist
#           if they do exist, read next record
#           if they don't exist, write them to a LIST 
#
#       4. as we are looping through the records, for each candidate +1 to their vote_tally
#       NOTE: we are at the end of this for-loop
#       5.
#       define another LIST having the candidate_name and their vote_percentage
#       so now, we take the results we have placed in our candidate_votes LIST and we take the candidates votes, 
#       divide them by total number of votes and multiply them by 100
#       
#       6. an if statement asking if the previous canditate's vote_tally is higher then the lasts within a for-loop

import csv
import os

# Input and Output Files
input_file = os.path.join("Resources", "election_results.csv")
output_file=os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(input_file) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


    # TODO: read and analyze the data here.
     
 
    # Create output
    with open(output_file, "w") as election_report:
    
        # Write list of three counties to the file.
        election_report.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    
        election_report.close()
    