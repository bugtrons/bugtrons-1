using System;

class bugtrons2
{

static int maxProfitofBitcoin(int []rate, int begin, int over)
{

    // If the bitcoins can't be bought
    if (over <= begin)
        return 0;

    // Initialise the profit
    int profit = 0;

    // The day at which the bitcoin must be bought
    for (int i = begin; i < over; i++)
    {

        // The day at which the bitcoin must be sold
        for (int j = i + 1; j <= over; j++)
        {

            // If buying the bitcoin at ith day and selling it at jth day is profitable
            if (rate[j] > rate[i])
            {

                // Update the current profit
                int curr_profit = rate[j] - rate[i]
                                + maxProfitofBitcoin(rate, begin, i - 1)
                                + maxProfitofBitcoin(rate, j + 1, over);

                // Update the maximum profit so far
                profit = Math.Max(profit, curr_profit);
            }
        }
    }
    return profit;
}

// Driver code
public static void Main(String[] args)
{
    int []rate = { 130, 210, 290, 340, 70, 565, 625 };
    int n = rate.Length;

    Console.Write(maxProfitofBitcoin(rate, 0, n - 1));
}
}
