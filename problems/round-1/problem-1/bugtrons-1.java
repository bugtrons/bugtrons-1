// Java code for Maximum Water Container

class bugtrons1{

public static int maxAreaofWaterContainer(int[] m)
{

    int Area = 0;
    
  for(int i = 0; i < m.length; i++)
    {
        for(int j = i + 1; j < m.length; j++)
        {
            // write your code here
        }
    }
    
    return Area;
}

// Driver code
public static void main(String[] args)
{
    int a[] = { 2, 6, 5, 4 };
    int b[] = { 4, 2, 3, 5, 6 };

    System.out.println(maxAreaofWaterContainer(a));
    System.out.println(maxAreaofWaterContainer(b));
}
}
