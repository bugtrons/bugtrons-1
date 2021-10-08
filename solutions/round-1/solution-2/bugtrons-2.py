def maxProfitofBitcoin(rate, begin, over):

    # If the bitcoins can't be bought
    if (over <= begin):
        return 0;

    # Initialise the profit
    profit = 0;

    # The day at which the bitcoin must be bought
    for i in range(begin, over, 1):

        # The day at which the bitcoin must be sold
        for j in range(i+1, over+1):

            # If buying the bitcoin at ith day and selling it at jth day is profitable
            if (rate[j] > rate[i]):
                
                # Update the current profit
                curr_profit = rate[j] - rate[i] +\
                            maxProfitofBitcoin(rate, begin, i - 1)+ \
                            maxProfitofBitcoin(rate, j + 1, over);

                # Update the maximum profit so far
                profit = max(profit, curr_profit);

    return profit;

# Driver code
if __name__ == '__main__':
    rate = [ 130, 210, 290, 340, 70, 565, 625];
    n = len(rate);

    print(maxProfitofBitcoin(rate, 0, n - 1));
