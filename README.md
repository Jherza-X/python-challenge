# python-challenge
Challenge three repository introduction to Python UofT Data Visualization bootcamp
Jesus E. Hernandez 

Location in of my code source in repository "python-challenge" for PyPoll and PyBank analysis:

python-challenge\PyPoll\main.py
python-challenge\PyBank\main.py

Both codes generate a txt file that stores in the next location respectively:

python-challenge\PyPoll\Analysis\PyPoll_Election_Results_Analysis.txt
python-challenge\PyBank\Analysis\PyBank_Financial_Analysis.txt

Commands for gitbash
1. git commit -m "comment" - commit all changes
2. git push origin main - tell the server
*********************************************************************************************************************************************
python-challenge\PyPoll\main.py  SOURCE CODE
Challenge three repository introduction to Python UofT Data Visualization bootcamp
Jesus E. Hernandez 
******************************************************************************************************************************
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

#variables initialization
Total_votes = 0
Candidate_list = []
Candidate_aux = []
count = 0
candidate_0 = 0
candidate_1 = 0
candidate_2 = 0
average_candit_0 = 0
average_candit_1 = 0
average_candit_2 = 0

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    #print(header)
    
    # Loop through the data
    for row in csvreader:
        #print(row)
        Total_votes += 1
        Candidate_list.append(row[2])
    
    # Loop to find the names of all the candidates
    for i in range(len(Candidate_list)-1):
        if Candidate_list[i+1] != Candidate_list[i]:
            if Candidate_list[i] not in Candidate_aux:
                Candidate_aux.append(Candidate_list[i])
    
    # Loop to find the number of votes for each candidate
    for i in range(len(Candidate_list)):
        if Candidate_aux[0] == Candidate_list[i]:   
            candidate_0 += 1
        elif Candidate_aux[1] == Candidate_list[i]:
            candidate_1 += 1
        elif Candidate_aux[2] == Candidate_list[i]:
            candidate_2 += 1


    #print(Candidate_list)

    #Average Calculation
    average_candit_0 = round((candidate_0*100)/Total_votes,3)
    average_candit_1 = round((candidate_1*100)/Total_votes,3)
    average_candit_2 = round((candidate_2*100)/Total_votes,3)


#******************print out Section ********************************************
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {Total_votes}")
    print("--------------------------")

    print(f"{Candidate_aux[0]} : {average_candit_0} % ({candidate_0})")
    print(f"{Candidate_aux[1]} : {average_candit_1} % ({candidate_1})")
    print(f"{Candidate_aux[2]} : {average_candit_2} % ({candidate_2})")
    print("--------------------------")
    print(f"Winer: {Candidate_aux[1]}")
    print("--------------------------")

#Export the results to a text file
#I used a list to store each string I want in the file 
    item1 = "Election Results"
    item2 = "-----------------------------------"
    item3 = f"Total Votes: {Total_votes}"
    item4 = "-----------------------------------"
    item5 = f"{Candidate_aux[0]} : {average_candit_0} % ({candidate_0})"
    item6 = f"{Candidate_aux[1]} : {average_candit_1} % ({candidate_1})"
    item7 = f"{Candidate_aux[2]} : {average_candit_2} % ({candidate_2})"
    item8 = "--------------------------"
    item9 = f"Winer: {Candidate_aux[1]}"
    item10 = "--------------------------"

#I filled up the list
    print_out_list = [item1,item2,item3,item4,item5,item6,item7,item8,item9,item10]
    #print(print_out_list)
 
 #Create a new file to store all the information in Resources/PyBank_Financial_Analysis.txt
    My_file_path = os.path.join('Analysis', 'PyPoll_Election_Results_Analysis.txt')   
    
#write the information in the file 
    with open(My_file_path, 'w') as file:  
        # Write each calculation to the file
        for calculation in print_out_list:
            file.write(calculation + '\n')
    print(f"Calculations have been saved to {My_file_path}")


*********************************************************************************************************************************************
python-challenge\PyBank\main.py  SOURCE CODE
Challenge three repository introduction to Python UofT Data Visualization bootcamp
Jesus E. Hernandez 
******************************************************************************************************************************

import os
import csv

#function definition 
#function that calculate the average rounding up to 2 decimal places
def average_change(first_value,last_value,num_values):
    ave_change = (last_value - first_value)/num_values
    return round(ave_change, 2)

#function difference substracts subsequent values in a list and returs a list with all the differences
# This function will help to calculate the greates increase and decrease 
def difference(my_list):
    result = []
    for i in range(len(my_list) - 1):
        diff =  int(my_list[i + 1]) - int(my_list[i])
        result.append(diff)
    return result


# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#Variables initialization 
aux = 0
Total_months = 0
Total_income = 0
average = 0
first_value = 0
aux_list1 = []
aux_list2 = []
substraction = []
Max_ave = 0
Min_ave = 0
print_out_list = []

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    #print(header)
    
    # Loop through the data
    for row in csvreader:
        #this conditional obtains the first value in row[1] to calculate the average
        if aux == 0:
            first_value = int(row[1])
            #print("got the first value")
            Total_months = Total_months + 1
            Total_income = Total_income + int(row[1])
        else:
            #Total of months calculation
            Total_months = Total_months + 1
            #Total amount of Profit/Loses
            Total_income = Total_income + int(row[1])
            #print("In Else")
        #print(f"here is the max -> {max_value}")
        aux = aux + 1
        #filling up auxiliar_list 1and 2 with row[0] and row[1] values this will 
        # help to calculate the increase and decrease in profits 
        aux_list1.append(row[1])
        aux_list2.append(row[0])



        #print(type(row))
        #print(row[1])
        
    #getting the last value of row
    last_value = int(row[1])    
    #print(f"here is the max -> {max_value}")


###############printing section Financial Analysis   *****************
    #print(row[1])
    
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months:  {Total_months}")
    print(f"Total:  ${Total_income}")    
    #print(f"Here last value-> {last_value}")
    #print(f"Here first value-> {first_value}")
    
    #function that return the average defined at the beginin 
    #average = average_change(first_value,last_value,Total_months)    
    #print(f"Average Change:  ${average}")
    #print(aux_list2)
    #use difference function to calculate the average change, increases, and decreases 
    substraction = difference(aux_list1)

    #This calculate the number the net change as the summation of the total 
    # month-to-month changes in all the rows over the total number of net changes 
    average = round(sum(substraction)/len(substraction),2)
    print(f"Average Change:  ${average}")


    #Using the fuction max to find the maximun value in substraction list 
    Max_ave = max(substraction)
    #index max gives the place of the maximun value found
    index_max = substraction.index(max(substraction))
    #Using the fuction min to find the maximun value in substraction list 
    Min_ave = min(substraction)
    #index min gives the place of the minimun value found
    index_min = substraction.index(min(substraction))
    #print(len(substraction))
    
    #to find the date for the max and min increses we use aux_list2 and index_max and index_min
    
    print(f"Greatest Increase in Profits: {aux_list2[index_max + 1]}  ({Max_ave})")
    #print(f"Max index is: {index_max}")
    #print(aux_list2[index_max + 1])
    
    print(f"Greatest Decrease in Profits: {aux_list2[index_min + 1]} ({Min_ave})")
    #print(f"Min index is: {index_min}")
    #print(aux_list2[index_min + 1])


#Export the results to a text file
#I used a list to store each string I want in the file 
    item1 = "Financial Analysis"
    item2 = "-----------------------------------"
    item3 = f"Total Months:  {Total_months}"
    item4 = f"Total:  ${Total_income}"
    item5 = f"Average Change:  ${average}"
    item6 = f"Greatest Increase in Profits: {aux_list2[index_max + 1]}  ({Max_ave})"
    item7 = f"Greatest Decrease in Profits: {aux_list2[index_min + 1]} ({Min_ave})"

#I filled up the list
    print_out_list = [item1,item2,item3,item4,item5,item6,item7]
    #print(print_out_list)
 
 #Create a new file to store all the information in Resources/PyBank_Financial_Analysis.txt
    My_file_path = os.path.join('Analysis', 'PyBank_Financial_Analysis.txt')   #"PyBank_Financial_Analysis.txt"

#write the information in the file 
    with open(My_file_path, 'w') as file:  
        # Write each calculation to the file
        for calculation in print_out_list:
            file.write(calculation + '\n')
    print(f"Calculations have been saved to {My_file_path}")




