# counties dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
'''
# iterating over a tupple to get keys of a dictionary
for county in counties_dict:
    print(county)

# This is more descriptive: 
# iterate over the dictionary using the keys()
for county in counties_dict.keys():
    print(county)
    
# this prints out the dictionaries 3 times   
for county in counties_dict:
    print(counties_dict.keys())

# Iterate over the dictionary using values() methed to get values    
for voters in counties_dict.values():
    print(voters)
    
# this gets VALUES!!!!! NOT the KEYS
for county in counties_dict:
    print(counties_dict[county])
    
# Using the get() method to get the values of a key
for county in counties_dict:
    print(counties_dict.get(county))


# using item() method to get key-value Pairs 
for county, voters in counties_dict.items():
    print(county, voters)
    
# NOTE:    
#The first variable declared in the for loop is assigned to the keys.
#The second variable is assigned to the values.

# SKILL DRILL
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")
'''
# This is a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
'''
# Iterate Through a List of Dictionaries
# Get Each Dictionary in a List of Dictionaries
for county_dict in voting_data:
    print(county_dict)

gives this: 

{'county': 'Arapahoe', 'registered_voters': 422829}
{'county': 'Denver', 'registered_voters': 463353}
{'county': 'Jefferson', 'registered_voters': 432438}    

# Since voting_data is a LIST of dictionaries, we can use the function range() to iterate over the list 

for i in range(len(voting_data)):
    print(voting_data[i])
'''
## THIS DOES NOT WORK BECAUSE counties_dict is not a LIST, it is a dictionary.
##for i in range(len(counties_dict)):
##    print(counties_dict[i])    
'''
# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values(): #commenting out this 
        print(value)
#         print(county_dict)           <uncommenting this , give us the dictionaries.

# First, use the for loop: for county_dict in voting_data: to retrieve each dictionary.
# Then, in the second for loop, use the values() method on the variable county_dict to 
# reference the data in the second for loop in order to get each value.        
# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438
'''
#Question
#How would you retrieve the number of registered voters from each dictionary?
# no this give BOTH values in the dictionary
'''
for county_dict in voting_data:  
     print(county_dict.values())
dict_values(['Arapahoe', 422829])
dict_values(['Denver', 463353])
dict_values(['Jefferson', 432438])
'''
# it isn't going to be a nested for loop on value (we just did this!)
'''
for county_dict in voting_data:    
   for value in county_dict:      
       print(value)

# it is this...DUH
for every_dictionary in voting_data:

     print(every_dictionary['registered_voters'])

#print the county name from each dictionary
for every_dictionary in voting_data:
    print(every_dictionary['county'])
'''


    
    