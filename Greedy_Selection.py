#Set up the libraries that I need
import numpy as np
import pandas as pd
from scipy.spatial import distance
#from scipy import stats

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

#print(stats.describe(teams_list))    
#print(stats.describe(relevant_rows))

#data2 = data[data['Obs_ID'].isin(relevant_rows)]
#data2.to_csv("relevant_rows.csv", index=False)

data = data[data['Obs_ID'].isin(relevant_rows)]
data.to_csv("relevant_rows.csv", index=False)

#Set some for loops to go through the departments
depts_list = data.Dept.unique()
incumbent_metric = 50000

for dept in depts_list:    
    #Count the exp / control group in the department for if statement
    teams = data[data['Dept'] == dept]
    e_teams = teams[teams['treatment'] == 1]
    c_teams = teams[teams['treatment'] == 0]
    count_e = len(e_teams)
    count_c = len(c_teams)
    print("dept: ",dept," total:", str(count_e + count_c)," Experimental: ", str(count_e),"  |  ", str(round(100*count_e/(count_e+count_c),3)),"%")

#Go through each experiment group in that dept
    for e in range(count_e):
        #calculate the metric for the c_teams:
        for c in range(count_c):
            e_team_array = np.array([e_teams['profit'].iloc[e],e_teams['size'].iloc[e],e_teams['wageindex'].iloc[e]])
            c_team_array = np.array([c_teams['profit'].iloc[c],c_teams['size'].iloc[c],c_teams['wageindex'].iloc[c]])
            current_metric = distance.euclidean(e_team_array,c_team_array)
            #Create some mechanism for there to be an incumbent
            if current_metric < incumbent_metric:
                incumbent_metric = current_metric
                #incumbent_id = cteams['id']
            
print(metric)
#find the control group with the least metric
#Create some Pairs
#Output the pairs