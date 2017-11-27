# Dwrite function to do calculations for using pandas
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
# final script should both print the analysis to the terminal and export a text file with the results

import pandas as pd
import numpy as np
import os

myinput = input("What is the election input file path? :")
outputfile= input("What should be your file name and desire output file path ?:")

#open the file
#myelectionfile= 'C:\Pri doc\priti\Projects\Myproject\Berkely\Week 3 Python\Homework python\poll\election_data_2.csv'
myelectionfile = myinput

def result(myfile):
    #open csvfile
    data= pd.read_csv(myfile)
    #total no of votes
    TotalVotes = data['Voter ID'].count()
    print("Total votes in elections:",TotalVotes)
    #unique candidates
    print ("Elcetion Candidates", data ['Candidate'].unique())
    #total votes for each candidate
    list = []
    list= data.groupby('Candidate')['Voter ID'].count()
   # print(list)
    #Each candidate votes:
   # print("List of candiate: ",list.values[1])
    ctotal=list.values
 #   print("Candiates votes :",ctotal)      
    pertotal=list.values/TotalVotes*100 
   # print("Percenage for each candiate:%" ,pertotal)
   # print("Max Voter percentage win:", max(pertotal))

    print("Election Results")
    print("----------------")
    print("Total Votes:",TotalVotes)
    print("----------------")
    df2 = pd.DataFrame({'Candidate' : list.keys() ,'TotalVotes' :ctotal, 'PercentVote':pertotal})
    print (df2.to_string(index=False))
    i=df2.iloc[df2['TotalVotes'].idxmax()]
    print("----------------")
    print("Winner :",i[0])
    print("----------------")

    #write to file 
    #new_path = 'C:\\Pri doc\\priti\\Projects\\Myproject\\Berkely\\Week 3 Python\\result.txt'
    new_path = outputfile
    myresult = open(new_path,'w')
    
    myresult.write("Election Results \n---------------- \n Total Votes:")
    myresult.write(str(TotalVotes))
    myresult.write("\n --------------- \n ")
    myresult.write( df2.to_string(index=False))
    myresult.write("\n ----------------\n Winner :")
    myresult.write(i[0])
    myresult.write("\n ----------------")

    myresult.close()




result(myelectionfile)