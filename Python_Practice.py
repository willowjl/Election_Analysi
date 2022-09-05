#counties = ["Arapahoe","Denver","Jefferson"]
#counties.insert(1,"El Paso")
#counties.remove("Arapahoe")
#counties.pop(1)
#counties.insert(2, counties.pop(len(counties)-1))
#counties.append("Arapahoe")
#counties.insert(1, "Denver")
#print(counties)

counties_dict ={}
counties_dict["Arapahoe"]= 422829
counties_dict["Denver"]= 463353
counties_dict["Jefferson"]= 432438
counties_dict.items()

voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
voting_data.append({"County":"El Paso", "registered_voters":461148})

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1]=='Denver':
    print(counties[1])

# WHat is the score
score=int(input("whst is your test score? "))

# Determien the grade
if score>= 90:
    print('Your grade is an A')
elif score>=80:
    print("Your grade is B")
elif score>=70:
    print('Your grade is C')
elif score>=60:
    print("Your grade is a D")
else:
    print('Your grade is an F')

counties=["Arapahoe", "Denver", "jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

counties=["Arapahoe", "Denver", "jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("only Arapahoe is in the list")
else:
    print("Arapahoe is in the list and el paso is not")

count = 7

while count < 1:

    print("Hello World")


counties=["Arapahoe", "Denver", "jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, voters)


voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
voting_data.append({"County":"El Paso", "registered_voters":461148})
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
#

my_votes=int(input("How many votes did you get? "))
total_votes=int(input("What was the total votes in the election?" ))
percent_votes=(my_votes/total_votes)*100
print(f"i received " + str(percent_votes)+ "% of the total votes")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")