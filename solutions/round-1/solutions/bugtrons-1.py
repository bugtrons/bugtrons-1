# Python3 code for Maximum Water Container

def maxArea(M, Length) :
    area = 0
    for i in range(Length) :
        for j in range(i + 1, Length) :
           
            # Calculating the max area
            area = max(area, min(M[j], M[i]) * (j - i))

    return area
 
# Driver code
a = [ 2, 6, 5, 4 ]
b = [ 4, 2, 3, 5, 6 ]
 
len1 = len(a)
print(maxArea(a, len1))
 
len2 = len(b)
print(maxArea(b, len2))
