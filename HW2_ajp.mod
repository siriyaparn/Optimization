#declare set 
set PRODUCT;

#declare parameter
param SALE{PRODUCT} >= 0;
param LABOR{PRODUCT} >= 0;
param PURCHASE{PRODUCT} >= 0;
param RAW_MAT >= 0;
param HOUR_MAX >= 0;

#create model
var x{PRODUCT} >= 0;    #x : the amount of product type i 
maximize ojective: sum{i in PRODUCT} (SALE[i]-(LABOR[i] * PURCHASE[i])) * x[i]; #find max profit
subject to subject1: sum{i in PRODUCT} x[i] <= RAW_MAT;                         #constraint 1 : raw mat availble <= 60
subject to subject2: sum{i in PRODUCT} LABOR[i]*x[i] <= HOUR_MAX;               #constraint 2 : labor can be purchased <= 90 