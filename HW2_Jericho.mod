#declare set 
set INTERVAL;

#declare parameter
param BUS_MIN{INTERVAL} >= 0;
param MOD_NUM >= 0;
param STEP >= 0;

#create model
var x{INTERVAL} >= 0;  #x : the amount of busses which start at the time of the day i
minimize Objective: sum{i in INTERVAL} x[i]; #find min busses
subject to subject {i in INTERVAL}: x[i] + x[(i mod MOD_NUM)+STEP] >= BUS_MIN[(i mod MOD_NUM)+STEP];
#constraint : the restriction that busses run for 8 hours
#Example : x[1] + x[(1 mod 6)+1] >= BUS_MIN[(1 mod 6)+1]
#                    x[1] + x[2] >= BUS_MIN[2]
#                    x[1] + x[2] >= 8
