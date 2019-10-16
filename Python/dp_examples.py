# calculate fibonacci numbers up to an nth number
def fibonacci(n): 
    fibonacci_array = [0]*(n+1) 
    # base case  
    fibonacci_array[1] = 1
    for i in range(2 , n+1): 
        fibonacci_array[i] = fibonacci_array[i-1] + fibonacci_array[i-2] 
    return fibonacci_array
print(fibonacci(12))

#0-1 Knapsack Problem O(mn)
#Transition Function: j≥wi,a[i,j]=a[i−1,j]∨a[i−1,j−wi].Otherwise,a[i,j]=a[i−1,j].
def knapsack(m, n):
    a[0,0] = True
    i = 1
    j = 1
    for j in m:
        a[0,j] = False
    for i in n:
        j = 0
        for j in m:
            return 0

#This problem finds the longest in a matrix of integers in which the path is in increasing order by one
def longestMatrixPath (i, j, matrix, dp ):
    n = len(matrix) #dimensionn of matrix
    #base case
    if (i<0 or i>= n or j<0 or j>=n):
        return 0
    if (dp[i][j] != -1):
        return dp[i][j]
    x, y, z, w = -1, -1, -1, -1 
    if (j < n-1 and ((matrix[i][j] + 1) == matrix[i][j+1])): 
        x = 1 + longestMatrixPath(i, j + 1, matrix, dp) 
  
    if (j > 0 and (matrix[i][j] + 1 == matrix[i][j-1])):  
        y = 1 + longestMatrixPath(i, j - 1, matrix, dp) 
  
    if (i > 0 and (matrix[i][j] + 1 == matrix[i-1][j])): 
        z = 1 + longestMatrixPath(i - 1, j, matrix, dp) 
  
    if (i < n-1 and (matrix[i][j] + 1 == matrix[i+1][j])): 
        w = 1 + longestMatrixPath(i + 1, j, matrix, dp) 
  
    # If none of the adjacent fours is one greater we will take 1 
    # otherwise we will pick maximum from all the four directions 
    dp[i][j] = max(x, max(y, max(z, max(w, 1)))) 
    return dp[i][j] 
  
def findLongestOverAll(matrix): 
    result = 1 # Initialize result
    n = len(matrix)  
  
    #  Lookup table filled as -1  
    dp =[[-1 for i in range(n)]for i in range(n)] 
  
    # Longest path from all cells
    for i in range(n): 
        for j in range(n): 
            if (dp[i][j] == -1): 
                longestMatrixPath(i, j, matrix, dp) 
            result = max(result, dp[i][j]);  
    return result 

adjaceny_matrix = [[0, 4, 1, 39], [3, 5, 6, 11], [10, 15, 7, 2], [10, 9, 8, 99]]
print("The longest path is:", findLongestOverAll(adjaceny_matrix))