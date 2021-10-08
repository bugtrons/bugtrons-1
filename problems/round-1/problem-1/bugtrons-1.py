# Python3 code for Maximum Water Container

def maxAreaofWaterContainer(M, Length) :
    area = 0
    for i in range(Length) :
        for j in range(i + 1, Length) :
           
            # write your code here

    return area
 
# Driver code
a = [ 2, 6, 5, 4 ]
b = [ 4, 2, 3, 5, 6 ]
 
len1 = len(a)
print(maxAreaofWaterContainer(a, len1))
 
len2 = len(b)
print(maxAreaofWaterContainer(b, len2))
