# the we need to retrieve.
#1. the total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidates won
#4. The tal numver of votes each candidte won.
#5. The winner of the election based on popular vote. 

# Add our dependencies
from calendar import c
import csv
import os

#Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes=0

#candidate options and candidate votes
candidate_options=[]

#1. initialize candidate votes
candidate_votes={}

#Winning candidate and winning count number
winning_candidate=""
winning_count=0
winning_percentage=0


#open the election results and read the file.
with open(file_to_load) as election_data:
    
#to do: read and analyze the file reader.
    file_reader=csv.reader(election_data)

    #read the header now
    headers=next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        #2. add to the total vote count
        total_votes+=1

        #declaring a list for the candidates
        candidate_name=row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add the candiate names to the candidate list
            candidate_options.append(candidate_name)

            #to track candidates vote count
            candidate_votes[candidate_name]=0

        #to track cnandidate votes
        candidate_votes[candidate_name]+=1

# Determine the percentage of votes for each candidate by looping through the chart
#1. iterate through the candidare list
    for candidate_name in candidate_votes:

            #2. Retrieve vote count for each candidate
            votes=candidate_votes[candidate_name]
          
            #3. Calcuclate the percentage
            vote_percentage=float(votes)/float(total_votes)*100

            #Determine the winning vote count and candidate
            #Determine if the votes are greater than the winning count.
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                    #if true then set the winning_count = votes and winning_percent
                    #vote_percentage.
                    winning_count=votes
                    winning_percentage=vote_percentage
                    #and, set the winning candidate equal to the candidate"s name.
                    winning_candidate=candidate_name

            # to do: print out the winning candidate, vote count and percentage to terminal.
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary=(
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}%\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")


print(winning_candidate_summary)
 #4. Print the candidate name and percentage of votes.
#            print(f"{candidate_name}: received {round(vote_percentage,1)}% of the votes.")

#3. Print total_votes        
#print(candidate_votes)

