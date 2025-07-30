class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n ,m  = len(matrix) , len(matrix[0])
        left, top, right, bottom = 0 ,0, m-1 , n-1
        arr = []

        while left <= right and top <= bottom:

            for i in range(left, right+1):
                arr.append(matrix[top][i])
            top += 1

           
            for i in range(top,bottom+1):
                arr.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1,-1):
                    arr.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    arr.append(matrix[i][left])
                left += 1

        return arr
        

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
