## Importing Necessary Dictionaries

import csv
from itertools import combinations 
import math
import sys

## ----------------------------------
## Part 1: Loading Data From CSV File

with open(sys.argv[3]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = []
    for row in csv_reader:
        data.append(row)
## -------------------------------------------
## Part 2: Transforming Data to make it useful

data = data[1:] 
symbol = []
close = []

for a in data:
    symbol.append(a[0])
    close.append(a[2])

# 'ref' contains the symbol of index to approximate
# 'ref_close' is a list containing all close for 'ref'

ref_close = []
for i in range(0,len(symbol)):
    if symbol[i] == sys.argv[2]:
        ref = symbol[i]
        ref_close.append(close[i])

for i in range(0,len(ref_close)):
    ref_close[i] = float(ref_close[i])

# 'symbol_ind' contains all other symbols (besides 'ref') --- List
# 'close_ind' contains all close values for all 'symbol_ind' --- List of Lists

total_symbol = int((len(data)/len(ref_close)) - 1)
total_data = len(ref_close)

symbol_ind = [" "]* total_symbol
close_ind = [[0.0 for i in range(total_data)] for j in range(total_symbol)]

start = len(ref_close)
for i in range(total_symbol):
    symbol_ind[i] = symbol[start+i]
    for j in range(total_data):
        close_ind[i][j] = float(close[start+j])
    start = start + total_data

## ----------------------------------------------------
## Part 3: Finding best approximate weights for n index

# 'gettingWeights' function takes input as 'ref_close' and 'close_ind' (associated with n indexes) 
# and provides the weights for each n.

def gettingWeights(ref_close, close_ind):
    n = len(close_ind)
    w = close_ind
    for i in range(0,len(ref_close)):
        A = ref_close[i]/n
        for j in range(0,len(close_ind)):
            w[j][i] = A/close_ind[j][i]
    final_w = []
    for a in w:
        final_w.append(Average(a))
    return final_w

# 'Average' function calculates average of a list (to be used in above gettingWeights function)

def Average(lst): 
    return sum(lst) / len(lst) 

# 'mean_square_error' function calculates mean square error between two lists.

def mean_square_error(A,B):
    msq = 0
    for i in range(0,len(A)):
        msq += (abs(A[i]- B[i]))**2
    msq = math.sqrt(msq)
    return msq

# The below code takes all possible combinations of 'n' indexes from the data.

n = int(sys.argv[1])
t = list(range(0,total_symbol))

comb = combinations(t, n) 
comb = list(comb)

# The below code calculates weights and calculates the least error (using Mean square method)
# for all 'n' combinations of indexes.

# It also stores the combination of symbols where we achieve least error. (to be used to print 
# as output) 

least_error = 10000000.0
for i in range(0,len(comb)):
    select_close = []
    for j in range(0,n):
        select_close.append(close_ind[comb[i][j]])
    final_weights = gettingWeights(ref_close, select_close)
    select_close2 = [[0.0 for ll in range(0,len(select_close[0]))] for kk in range(n)] 
    for k in range(n):
        for l in range(0,len(select_close[k])):
            select_close2[k][l] = select_close[k][l] * final_weights[k]    
    final_close = [0]*len(select_close[0])
    for m in range(0,len(select_close[0])):
        for x in range(0,len(select_close)):
            final_close[m] = final_close[m] + select_close2[x][m]
    err = mean_square_error(ref_close,final_close)
    if err < least_error:
        least_error = err
        best_ele = comb[i]
        best_weight = final_weights

## ----------------------------------------------------
## Part 4: Arranging Output Data in the correct Format to Print to Console

last_symbol = []
for itemsk in best_ele:
    last_symbol.append(symbol_ind[itemsk])
for itemsw in range(0,len(best_weight)):
    best_weight[itemsw] = round(best_weight[itemsw],2)

final_output = [[" " for xx in range(2)] for yy in range(0,len(last_symbol)+1)]
final_output[0][0] = "Symbol"
final_output[0][1] = "Weight"
for ii  in range(1,len(final_output)):
    final_output[ii][0] = last_symbol[ii-1]
    final_output[ii][1] = str(best_weight[ii-1])

final_output2 = [" " for sd in range(0,len(final_output))]
for jj in range(0,len(final_output)):
    final_output2[jj] = ','.join(final_output[jj])

print(*final_output2, sep = "\n")    






    

