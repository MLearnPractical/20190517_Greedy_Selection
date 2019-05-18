# 20190517_Greedy_Selection
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

Constraint 2: a control team can not be matched twice, unless the number of the experimental teams is bigger than the number of controls teams in this department

Constraint 3: profit, size, wage index three variables can be calculated the similarity

Constraint 4: using the first year of data in the calculation for each team

Constraint 5: using "Euclidean distance" to calculate similarity 

In addition to the above constraints, if you are uncertain about some steps, you can choose your own approach, but you have to write the explanatory notes.

[Requirements] use the programming language you are familiar with (such as R, Python, C ++), code independently (do not use existing formula of Greedy Matching). Last, submit your code in any form.

[1]   About Greedy Matching, you can reference the information here: https://www.statisticshowto.datasciencecentral.com/greedy-algorithm-matching/