#import libraries
import os
import csv

#define value to variables
countMonth =0
previousProfit=0
netTotalAmount =0
averageProfitChange=0

#declaring empty list 
dateValues=[]
profitValues=[]
averageProfitChangeValue=[]


csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
	csvread_budget =csv.reader(csvfile,delimiter=',')
	csv_header = next(csvread_budget)


	for row in csvread_budget:
		#count months in data
		countMonth+=1
		dateValues.append(row[0])
		profitValues.append(int(row[1]))
		#net total amount of "Profit/Losses" over the entire period
		netTotalAmount = netTotalAmount + int(row[1])
	for i in range(1,len(profitValues)):
		#print("sr no",i,profitValues[i])
		profitChange = profitValues[i]-profitValues[i-1]
		averageProfitChangeValue.append(profitValues[i]-profitValues[i-1])
	#average of Change in profit and Loss values over the period of year
	averageProfitChange=round(sum(averageProfitChangeValue)/(countMonth-1),2)
	#greatest increase & decrease in profits
	maxIncrease = max(averageProfitChangeValue)
	maxDecrease = min(averageProfitChangeValue)

	#index of max and min
	index_maxIncrease = averageProfitChangeValue.index(maxIncrease)+1
	index_maxDecrease = averageProfitChangeValue.index(maxDecrease)+1

	#condition for matching indexes and printing date
	for j in range(len(dateValues)):
		if j==index_maxIncrease :
			monthDay_maxIncrease = dateValues[j]
		elif j==index_maxDecrease :
			monthDay_maxDecrease = dateValues[j]
	
print("Financial Analysis")
print("----------------------------")
print("Total Months: ",countMonth)
print("Total: $",netTotalAmount)
print("Average Change: $",averageProfitChange)
print("Greatest Increase in Profits:",monthDay_maxIncrease,"($", maxIncrease,")")
print("Greatest Decrease in Profits:",monthDay_maxDecrease,"($",maxDecrease,")")

#Write the output to text file
txtfile_Path = os.path.join('analysis','Financial_Analysis.txt')
with open(txtfile_Path, "w") as textFile:
	textFile.write("Financial Analysis\n")
	textFile.write("----------------------------\n")
	textFile.write(f"Total Months:{countMonth}\n")
	textFile.write(f"Total: ${netTotalAmount}\n")
	textFile.write(f"Average Change: ${averageProfitChange}\n")
	textFile.write(f"Greatest Increase in Profits: {monthDay_maxIncrease} (${maxIncrease})\n")
	textFile.write(f"GGreatest Decrease in Profits: {monthDay_maxDecrease} (${maxDecrease})\n")