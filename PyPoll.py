# the we need to retrieve.
#1. the total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidates won
#4. The tal numver of votes each candidte won.
#5. The winner of the election based on popular vote. 

# Add our dependencies
import csv
import os


#Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


#open the election results and read the file.
with open(file_to_load) as election_data:
    
    #print the election data
    #print(election_data)


# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#traceback (most recent call last):
#  File "PyPoll.py", line 24, in <module>
#open(file_to_save, "w")

#create a file name variable to a direct or indirect path to the file
#file_to_save=os.path.join("analysis", "election_analysis.txt")

#use the open statement to open the file as a text file
#outfile = open(file_to_save, "w")
#with open(file_to_save, "w") as txt_file:
#write some data to the file 
#outfile.write("Hello World")
#with open(file_to_save,"w") as txt_file:

#close the file_to_load
#outfile.close()
    #txt_file.write("Hello World")

# Write 3 counties to file
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #xt_file.write("Jefferson")
#    txt_file.write("Arapahoe\nDenver\nJefferson")

#to do: read and analyze the file reader.
    file_reader=csv.reader(election_data)

    #read and print the header now
    headers=next(file_reader)
    print(headers)