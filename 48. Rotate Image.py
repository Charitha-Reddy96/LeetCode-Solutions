#Brute Force approach

def rotate(matrix):
    mat = []
    n = len(matrix)
    count  = n-1
    for i in range(n):
        arr = []
        for j in range(n-1,-1,-1):
            arr.append(matrix[j][count])
        count -=  1   
        mat.append(arr)
    mat.reverse()
    return mat


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
#Output: [[7,4,1],[8,5,2],[9,6,3]]
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)

#Optimal Approach

def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i):
            matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
    for i in range(n):
        l , r = 0, n-1
        while l<r:
            matrix[i][l] , matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
    return matrix      
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))

#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#Time Complexity: O(n^2)
#Space Complexity: O(1)
