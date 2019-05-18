#Set up the libraries that I need
import numpy as np
import pandas as pd
from scipy.spatial import distance
from scipy import stats

#Import the CSV File
data = pd.read_csv("simulated_data.csv")
#print(data.head())

#Remove the lines from the CSV files that I don't need
#This gives the unique team values
teams_list = data.id.unique()
relevant_rows = np.array([])

for item in teams_list:
    team = data[data['id'] == item]
    team.sort_values(by=['year'])
    added = 0
#    print(team[['Obs_ID','treatment']])
    
    for index, row in team.iterrows():
        if row['treatment'] == 1:
            relevant_rows = np.append(relevant_rows, row['Obs_ID'])
            added = 1
            break
    
    if added == 0:
        new_value = team['Obs_ID'].iloc[0]
        relevant_rows = np.append(relevant_rows, new_value)    

print(stats.describe(teams_list))    
print(stats.describe(relevant_rows))

data2 = data[data['Obs_ID'].isin(relevant_rows)]
data2.to_csv("relevant_rows.csv", index=False)
#print(relevant_rows.describe())

#Set some for loops to go through the departments
#Count the exp / control group in the department for if statement
#Go through each experiment group in that dept
#find the control group with the least metric
#Create some Pairs
#Output the pairs