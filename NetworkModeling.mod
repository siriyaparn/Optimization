#declare set 
param NumNode = 4;
set Node := 1..NumNode;

#declare parameter
param cost{i in Node, j in Node};
param demand{i in Node};

#create model
var flow{i in Node, j in Node} >= 0;
minimize tripcost: sum{i in Node, j in Node} flow[i,j] * cost[i,j];
subject to subject{i in Node}: sum{h in Node} flow[h,i] - sum{j in Node} flow[i,j] = demand[i];