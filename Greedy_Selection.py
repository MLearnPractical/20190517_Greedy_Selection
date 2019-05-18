#Set up the libraries that I need
import pandas as pd
import numpy as np

#Import the CSV File
data = pd.read_csv("simulated_data.csv")
#print(data.head())

#Remove the lines from the CSV files that I don't need
#This gives the unique team values
teams_list = data.id.unique()

for team in teams_list:
    print(data[data['id'] == team])

#***
#for team in teams_list:
#    for record in data.loc:
#        if record.id[] == team:
#/

#Set some for loops to go through the departments
#Count the exp / control group in the department for if statement
#Go through each experiment group in that dept
#find the control group with the least metric
#Create some Pairs
#Output the pairs