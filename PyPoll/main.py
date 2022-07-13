#import libraries
import os
import csv

#initialize variable 
votesCasted = 0
countCand_1 = 0
countCand_2= 0
countCand_3 = 0

#Create empty list
candidateName=[]
recievedVotes=[]

#Create dictionary for finding winner
newDict={}


csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
	csvread_election =csv.reader(csvfile,delimiter=',')
	csv_header = next(csvread_election)
	
	for row in csvread_election:
		votesCasted+= 1
		candidateName.append(row[2])
	#logic for finding name of each candidates
	for i in range(len(candidateName)):
		if candidateName[i] not in recievedVotes:
			recievedVotes.append(candidateName[i])
			# print to check how many unique candidate we have in data 
			#print(recievedVotes)
		if (candidateName[i] == recievedVotes[0]):
			countCand_1+=1	 
		elif (candidateName[i] == recievedVotes[1]):
			countCand_2+=1		
		else : 
			countCand_3+=1

	#percentage votes 
	percentCand_1=round(countCand_1/votesCasted*100,3)
	percentCand_2=round(countCand_2/votesCasted*100,3)
	percentCand_3=round(countCand_3/votesCasted*100,3)
	
	#Creating dictionary to find the winner
	newDict={recievedVotes[0]:countCand_1,recievedVotes[1]:countCand_2,recievedVotes[2]:countCand_3}
	winner =max(newDict,key=newDict.get)
	
	print("Election Results")
	print("-------------------------")
	print(f"Total Votes: {votesCasted}")
	print("-------------------------")
	print(f"{recievedVotes[0]}: {percentCand_1}% ({countCand_1})")
	print(f"{recievedVotes[1]}: {percentCand_2}% ({countCand_2})")
	print(f"{recievedVotes[2]}: {percentCand_3}% ({countCand_3})")
	print("-------------------------")
	print(f"Winner: {winner}")
	print("-------------------------")


	#Write the output to text file
	txtfile_Path = os.path.join('Election_Results.txt')
	with open(txtfile_Path, "w") as textFile:
		textFile.write("Election Results\n")
		textFile.write("----------------------------\n")
		textFile.write(f"Total Votes: {votesCasted}\n")
		textFile.write("----------------------------\n")
		textFile.write(f"{recievedVotes[0]}: {percentCand_1}% ({countCand_1})\n")
		textFile.write(f"{recievedVotes[1]}: {percentCand_2}% ({countCand_2})\n")
		textFile.write(f"{recievedVotes[2]}: {percentCand_3}% ({countCand_3})\n")
		textFile.write("----------------------------\n")
		textFile.write(f"Winner: {winner}\n")
		textFile.write("----------------------------\n")