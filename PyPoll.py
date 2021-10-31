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

# count for input file records initialized
total_votes = 0 

# Winner's Information
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# LIST of candidates: 
candidate_options = []
#Candidate's vote count DICTIONARY
candidate_votes = {}


# Open the election results and read the file
with open(input_file) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read header record
    headers = next(file_reader)
    
    # main
    for each_vote in file_reader:
        # counting total records
        total_votes += 1 
        
        # get the candidates name (used in accumulating votes)
        candidate_name = each_vote[2]

        if candidate_name not in candidate_options:
            # add name to the candidate_options LIST
            candidate_options.append(candidate_name)
            # INSTANTIATE a candidate as a key for dictionary candidate_votes
            candidate_votes[candidate_name] = 0
        
        # count a vote for candidate read    
        candidate_votes[candidate_name] += 1
        
    # Getting Percentage of Votes: 

    # get candidate names
    for each_candidate in candidate_votes: 
        # retrieve tallied vote for candidate
        votes = candidate_votes[each_candidate]
        
        # get the percentage for this candidate's votes
        vote_percent = float(votes)/float(total_votes) * 100

        print(f"{each_candidate}: {vote_percent:.1f}% ({votes:,})\n")
                
        # Test Scenario4: Correct percentage of each candidate's vote
        # print(f"{each_candidate}: recieved {vote_percent:.1f}% of the vote.")
        
        # finding the winner of the election
        if votes > winning_count and vote_percent > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percent
            winning_candidate = each_candidate

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
            
# Test Scenario5: The winner data
#print(f"The winner is {winning_candidate}")        
            
                
# Test Scenario1: Correct record count. Is 369711?
#print(total_votes)

# Test Scenario2: Correct candidates are in candidate_options: [Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane]
#print(candidate_options)

# Test Scenario3: Instantiated candidate name as key in candiatates_votes = {}
#print(candidate_votes)


            
            
            
           
'''
    # TODO: read and analyze the data here.
     
 
    # Create output
    with open(output_file, "w") as election_report:
    
        # Write list of three counties to the file.
        election_report.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    
        election_report.close()
'''    