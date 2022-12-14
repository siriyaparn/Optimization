set PRODUCT;
param SALE{PRODUCT} >= 0;
param LABOR{PRODUCT} >= 0;
param PURCHASE{PRODUCT} >= 0;
param RAW_MAT >= 0;
param HOUR_MAX >= 0;

var x{PRODUCT} >= 0;
maximize ojective: sum{i in PRODUCT} (SALE[i]-LABOR[i]) * x[i];
subject to subject1: sum{i in PRODUCT} x[i] <= RAW_MAT;
subject to subject2: sum{i in PRODUCT} LABOR[i]*x[i] <= HOUR_MAX;