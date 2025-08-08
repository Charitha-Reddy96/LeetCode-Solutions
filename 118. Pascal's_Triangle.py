class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        li.append([1])
        for i in range(1,numRows):
            temp = []
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    temp.append(1)
                    j += 1
                else:
                    temp.append(li[i-1][j-1] + li[i-1][j])
                    j+=1
            li.append(temp)
        return li


#Time Complexity: O(n^2)
#Space Complexity: O(n)
# if n = 5 - Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]