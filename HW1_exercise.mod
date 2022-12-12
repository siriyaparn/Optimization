set EXERCISE; #declare set EXERCISE
set LIMIT;    #declare set LIMIT
param Cal {EXERCISE} >= 0;      #calories of each exercises >= 0
param T_min {EXERCISE} >= 0;    #tolerance_min of each exercises >= 0
param T_max {i in EXERCISE} >= T_min[i]; #tolerance_max >= tolerance_min
param Burn_off >= 0;            #Burn_off >= 0 
param Hour_limit >= 0;          #Hour_limit >= 0

var T_spend {i in EXERCISE} >= T_min[i], <= T_max[i]; #variable label : T_spend (each exercises have limit tolerance)
minimize Hour_min: sum{i in EXERCISE} T_spend[i];     #objective label : to minimize exercises hours/week
subject to subject1 : sum{i in EXERCISE} Cal[i] * T_spend[i] >= Burn_off;  #constriant label : burn off >= 2000 
subject to subject2 : sum{i in LIMIT} T_spend[i] <= Hour_limit;            #constraint label : no more than 4 hours total of set LIMIT 

