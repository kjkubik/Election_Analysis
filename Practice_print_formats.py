#The different print methods we will cover are the print() function, 
# printing single and multiline f-strings, and formatting numbers 
# in print statements.

# no we didn't do this: 
#2.	A string with integer values converted 
# to a string using concatenation with the
# "+" sign. For example: print("Your interest for the year is $" + str(interest)) .

#F-strings: Formatted String Literals
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# Using F-Strings with Dictionaries
'''

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


#If we use f-stings, we can rewrite the print statement to be more intuitive and clear.

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
'''    
#Multiline F-Strings
#you need to tell a candidate how many votes they won, the total number 
# of votes, and the percentage of votes they received. You can use the 
# code you wrote to calculate the percentage of votes and create a message 
# to be printed to a screen, like this:
'''
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
'''

# Format Floating-Point Decimals
#The general format for a number to format it in an f-string is as follows:
# f'{value:{width},.{precision}}'
#
# Example: 
# message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

'''
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
'''    
    
    
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}] 

for every_dictionary in voting_data:
  #  for value in every_dictionary.values(): 
  #      print(value)

  print(f"{every_dictionary['county']} county has {every_dictionary['registered_voters']:,} registered voters.")
    