# 20190517_Greedy_Selection
This problem was asked to me by a fellow student having encountered it in an interview.  I've created this repository to attempt to solve the same problem and hopefully help that student to be equipped to answer similar questions successfully in the future.
-Falsedichotomancer

Coding Interview Problem - Greedy Segmentation of Control/Test without Replacement
[Background] In order to maintain the performance of the organization, a company has decided to implement a new management reform. This reform has been implemented in some teams. As a data scientist in PA team, in order to study the causal impact of this reform, we have gathered the data in the appendix (see Appendix 1):

Id - Team ID

Year - each year

Dept - Dept/Team code

Treatment - whether the reform has been implemented in the year, "1" means the implementation of the reform, as the "experimental team"; "0" means non-implementation of the reform, as the "control team". On the first year, if the treatment variable is "1", the following years showed "0", still considered as "the experimental team".

Profit - Team profits

Size - how many people in the team

Wage index - Salary Index

[Task] what you need to do is the matching part in "causal inference": Use Greedy Matching [1] approach for all experimental teams (the teams that have been implemented the reform) to find the most matching control groups (teams that have not been implemented the reforms) that have most similarities.

Constraint 1: matching teams can only happen within the same department
#Taking care of this with a for loop

Constraint 2: a control team can not be matched twice, unless the number of the experimental teams is bigger than the number of controls teams in this department
#If statement to see check if the number of experimental teams is bigger than the numberf of control teams
#

Constraint 3: profit, size, wage index three variables can be calculated the similarity

Constraint 4: using the first year of data in the calculation for each team

Constraint 5: using "Euclidean distance" to calculate similarity 
#Use the difference between the experimental group and the control groups to find the control group with the lowest metric for any given exp group.

In addition to the above constraints, if you are uncertain about some steps, you can choose your own approach, but you have to write the explanatory notes.

[Requirements] use the programming language you are familiar with (such as R, Python, C ++), code independently (do not use existing formula of Greedy Matching). Last, submit your code in any form.

[1]   About Greedy Matching, you can reference the information here: https://www.statisticshowto.datasciencecentral.com/greedy-algorithm-matching/
