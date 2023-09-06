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
