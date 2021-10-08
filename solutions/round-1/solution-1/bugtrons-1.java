// Java code for Maximum Water Container

class bugtrons1{

public static int maxArea(int[] m)
{

    int Area = 0;
    
  for(int i = 0; i < m.length; i++)
    {
        for(int j = i + 1; j < m.length; j++)
        {
            // write your code here
            Area = Math.max(
                Area, Math.min(m[i], m[j]) *
                            (j - i));
        }
    }
    
    return Area;
}

// Driver code
public static void main(String[] args)
{
    int a[] = { 2, 6, 5, 4 };
    int b[] = { 4, 2, 3, 5, 6 };

    System.out.println(maxArea(a));
    System.out.println(maxArea(b));
}
}
