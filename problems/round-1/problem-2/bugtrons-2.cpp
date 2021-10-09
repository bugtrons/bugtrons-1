#include <bits/stdc++.h>
using namespace std;

int maxProfitofBitcoin(int rate[], int start, int end)
{
  // Write your code here 
}

// Driver code
int main()
{
	int rate[] = { 130, 210, 290, 340, 70, 565, 625 };
	int n = sizeof(rate) / sizeof(rate[0]);

	cout << maxProfitofBitcoin(rate, 0, n - 1);

	return 0;
}
