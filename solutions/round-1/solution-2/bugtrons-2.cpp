#include <bits/stdc++.h>
using namespace std;

int maxProfitofBitcoin(int rate[], int start, int end)
{

    // If the bitcoins can't be bought
    if (end <= start)
        return 0;

    // Initialise the profit
    int profit = 0;

    // The day at which the bitcoin must be bought
    for (int i = start; i < end; i++) {

        // The day at which the bitcoin must be sold
        for (int j = i + 1; j <= end; j++) {

            // If buying the bitcoin at ith day and selling it at jth day is profitable
            if (rate[j] > rate[i]) {

                // Update the current profit
                int curr_profit = rate[j] - rate[i]
                                + maxProfitofBitcoin(rate, start, i - 1)
                                + maxProfitofBitcoin(rate, j + 1, end);

                // Update the maximum profit so far
                profit = max(profit, curr_profit);
            }
        }
    }
    return profit;
}

// Driver code
int main()
{
    int rate[] = { 130, 210, 290, 340,
                    70, 565, 625 };
    int n = sizeof(rate) / sizeof(rate[0]);

    cout << maxProfitofBitcoin(rate, 0, n - 1);

    return 0;
}
