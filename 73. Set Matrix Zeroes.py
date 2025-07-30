#Optimal Solution

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        places = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    places.append((i,j))

        for i,j in places:
            for k in range(n):
                matrix[i][k] = 0
            for k in range(m):
                matrix[k][j] = 0
        return matrix

#Time Complexity : O(m*n)
#Space Complexity : O(m+n) for storing the places of zeroes


#Navie or Brute Force Approach
import math
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k]!= 0:
                            matrix[i][k] = float('inf') 
                    for k in range(m):
                        if matrix[k][j]!= 0:
                            matrix[k][j] = float('inf')
         
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
                    
#Time Complexity : O(m*n)*(m+n)
#Space Complexity : O(1)


                