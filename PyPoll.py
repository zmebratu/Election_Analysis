#1. # of the data we need to retrive

#2. total number of votes cast

#3. complete list of candidates who recieved votes 

#4. % of votes each candidate won 

#5. total # of votes each candidate won

#6. winner of the election based on popular vote 

# Assign a variable for the file to load and the path
file_to_load = 'Desktop/Election_Analysis/Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Desktop", "Election_Analysis", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


   