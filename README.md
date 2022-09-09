# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local
congressional election.

1.Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4.Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code, 1.71.0

## Summary
The analysis of the election show that:
There were 369,711 votes cast in the election.
- The candidates were:
- Candidate 1 - Charles Casper Stockman
• Candidate 2 - Diana DeGette
- Candidate 3 - Raymon Anthony Doane

The candidate results were:
Candidate 1 received 23% of the vote and 85,213 number of votes.
Candidate 2 received 73.8% of the vote and 272,892 number of votes.
Candidate 3 received 3.1% of the vote and 11,606 number of votes.

The winner of the election was:
Candidate 1, Diana DeGette, with ~74% of the total votes and 272,892 number of votes.

#Challenege Overview

##Overview of Election Audit: Explain the purpose of this election audit analysis.
### The election Audit challenge was a simple task that demanded a good understanding of the Python Programming language. The task was to analyze a CSV file containing raw election data for 3 counties and 3 candidates. The output of that analysis would help determine the voting ratio for all each county and each candidate. In addition, the analysis would also provide the winnning candidate and the county with the biggest voter.

##Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

###   How many votes were cast in this congressional election?
###   A total of 369,711 votes were casted during the congressional election.
###    Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    ![Voting Distribution](/main/votingDistribution.png)
###    Which county had the largest number of votes?
###    The county with largest number of votes is Denver with 306,055 votes, gathering 82.8% of the total votes across all 3 counties.
###    Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    ![Candidte Distribution](/main/CandidateDistribution.png)
###    Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
###    Diana DeGette ~~Anyone but Trump~~ won the election with 272,892 votes, 73.8% of the total voters.

## Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
### The challenge script can be refactored to calculate general presidential election for the country. The data would be a lot bigger in that case. The formula to determine the winning president would be updated to reflect the constitution requirement. Instead of just popular votes, we would need to capture which candidate received 270 votes from the electoral college, more than half of all electors in the country.
### On a smaller scale, the same script could be use to determine local mayors' election result for numerous town.

