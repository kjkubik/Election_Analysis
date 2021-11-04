import csv
import os

# input file(s):
file_to_load = os.path.join("Resources", "election_results.csv")
# output file(s):
file_to_save = os.path.join("analysis", "election_data.txt")

# capture candidate data 
candidate_names = []
candidate_votes = {}

# capture county data 
county_names = []
county_votes = {}

# vote counter.
total_votes = 0

# winning candidate stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# county with largest voter turnout
largest_county = ""
largest_county_count = 0
largest_county_percentage = 0

# get input needed to print report
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # header not needed
    header = next(reader)

    # do the following for each record
    for row in reader:

        # accumulate all votes
        total_votes = total_votes + 1

        # COUNTY: 
        # capture county names
        county_name = row[1]
                
        # add county name to county list if it doesn't exist
        if county_name not in county_names:
            candidate_names.append(county_name)

            # adding to county list
            county_names.append(county_name)
            
            # Test 1: counties are getting moved to county_names
            # print(county_names)

            # initialize vote count for county
            county_votes[county_name] = 0
            # Test 2: a county's vote count is initialized before counting votes
            # print(county_votes) 

        # accumulate county's vote count
        county_votes[county_name] += 1
        # Test 3: county's vote is accumulated correctly (run once!)
        # print(county_votes)
        
        # CANDIDATE
        # capture candidate name
        candidate_name = row[2]
               
        # add candidate name to candidate list if it doesn't exist
        if candidate_name not in candidate_names:

            # adding to candidate list
            candidate_names.append(candidate_name)
            # Test 4: candidate name is going to candidate names
            # print(candidate_names)

            # initialize vote count for candidate
            candidate_votes[candidate_name] = 0
            # Test 5: a canditate's vote count is initialize before using to count
            # print(candidate_votes)
            
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # Test 6: candidates votes are accumulating (do only one time!)
        # print(f"Canditate name and votes:{candidate_votes}")


# display and save generated report to file
with open(file_to_save, "w") as txt_file:

    # final vote count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    
    print(election_results, end="")
    txt_file.write(election_results)

    # looping through county dictionary
    for county_name in county_votes:
        # get county vote count
        county_vote_count = county_votes.get(county_name)
        # calculate the percentage of votes for the county 
        county_vote_percentage = float(county_vote_count)/float(total_votes) * 100 

         # county's results 
        county_results = f"{county_name}: " \
            f"{county_vote_percentage:.1f}% " \
            f"({county_vote_count:,})"
            
        print(county_results)
        txt_file.write(county_results)
            
        # determine winning county's namme (TODO: we could give the county's vote and percent)
        if (county_vote_count > largest_county_count) and (county_vote_percentage > largest_county_percentage):
            # we must keep the count and percent in sync for if statement
            largest_county_count = county_vote_count
            largest_county_percentage = county_vote_percentage
            largest_county = county_name

    # largest turnout
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        #f"County's Vote Count: {largest_county_count:,}\n"
        #f"County's Percentage: {largest_county_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(largest_county_summary)
    txt_file.write(largest_county_summary)

    # finals for candidates 
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # canditate's results
        candidate_results = f"{candidate_name}: " \
                            f"{vote_percentage:.1f}% " \
                            f"({votes:,})\n"

        print(candidate_results)
        txt_file.write(candidate_results)

        # determine winning candidate's vote count and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
