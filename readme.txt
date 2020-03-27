
================================================================================
How To Run The Code:

Your script should be invoked like so:

python3 approximate_index.py [n] [symbol of index to approximate] [historical prices csv]

For instance,

python3 approximate_index.py 3 .DJI dow_jones_historical_prices.csv

Please Note the Following:
1. The [historical prices csv] must exist in the same directory
2. [symbol of index to approximate] must exist in the [historical prices csv]
3. [n] must be greater than 1 to have a meaningful output.
4. The format for [historical prices csv] file must be same as what was described in the website.
http://interview.sgcaptrading.com/

================================================================================
Brief Coding Logic:

1. After Loading and Transforming the data, the code calculates weights for all possible combinations of n symbols. 
2. Weights is caulated by approximating the weighted individual sum of each symbol to the 'close' value of given symbol of index (i.e. the 3rd argument).
3. The combination which has the least mean square error is chosen as best combination of symbols. 
4. The weights values are rounded to 2 decimal points to be printed to console.