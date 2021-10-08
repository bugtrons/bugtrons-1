// C# code for Max
// Water Container

using System;
class bugtrons1
{

public static int maxArea(int[] m)
{

    int Area = 0;
    
    for(int i = 0; i < m.Length; i++)
    {
        for(int j = i + 1; j < m.Length; j++)
        {
            Area = Math.Max(Area, Math.Min(m[i], m[j]) *
                            (j - i));
        }
    }
    return Area;
}

// Driver code
public static void Main(String[] args)
{
    int []a = { 2, 6, 5, 4 };
    int []b = { 4, 2, 3, 5, 6 };

    Console.WriteLine(maxArea(a));
    Console.Write(maxArea(b));
}
}
