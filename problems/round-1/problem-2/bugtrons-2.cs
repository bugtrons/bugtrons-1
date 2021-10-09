using System;

class bugtrons2
{

static int maxProfitofBitcoin(int []rate, int begin, int over)
{
  // Write your code here 
}
// Driver code
public static void Main(String[] args)
{
	int []rate = { 100, 180, 260, 310,
					40, 535, 695 };
	int n = rate.Length;

	Console.Write(maxProfitofBitcoin(rate, 0, n - 1));
}
}
