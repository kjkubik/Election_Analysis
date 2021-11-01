import csv
import os

# input and output Files
input_file = os.path.join("Resources", "election_results.csv")
output_file=os.path.join("analysis", "election_analysis.txt")

# initialize total vote counter
total_votes = 0 

# winner's information
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# list of candidates: 
candidate_options = []
#candidate's vote count dictionary
candidate_votes = {}

# open the election results and read the file
with open(input_file) as election_data:

    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read header record
    headers = next(file_reader)
    
    # for each record count total votes, get all candiate's names,
    # and the number of votes for each candidate
    for each_vote in file_reader:
        
        total_votes += 1 
        
        candidate_name = each_vote[2]

        # add name to candidate_options list and instantiate a 
        # candidate as a key for candidtate_votes dictionary
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # counting votes for candidate
        candidate_votes[candidate_name] += 1
        
        
# open output file for election's analysis
with open(output_file, "w") as election_report:

    # reporting results
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    
    print(election_results, end="")
    election_report.write(election_results)

    # for each candidate find the percentage of votes 
    for each_candidate in candidate_votes: 
        # retrieve tallied vote values for candidate
        votes = candidate_votes[each_candidate]
            
        # get the percentage for this candidate's votes
        vote_percent = float(votes)/float(total_votes) * 100
        
        # create detail line
        candidate_results = (f"{each_candidate}: {vote_percent:.1f}% ({votes:,})\n")
        # terminal print of detail line
        print(candidate_results)
        # write detail line
        election_report.write(candidate_results)

        # keep track of who is winning
        if votes > winning_count and vote_percent > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percent
            winning_candidate = each_candidate

    # reporting winner: 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    election_report.write(winning_candidate_summary)