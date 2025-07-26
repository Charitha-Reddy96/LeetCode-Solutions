#Longest Consective Sequence

#Brute Force or Navie Approach

def linearsearch(n,nums):
        if n in nums:
            return True
        else:
            return False
def longestConsecutive( nums: list[int]) -> int:
        count = maxi = 0
        for i in range(len(nums)):
            x = nums[i]
            count = 1
            while (linearsearch(x+1,nums) == True):
                count += 1
                x += 1
            maxi = max(maxi,count)
        return maxi
        
nums = list(map(int,input().split(",")))
print(longestConsecutive(nums)) #input : 100,4,200,1,3,2
#Output : 4

#Time Complexity : O(n^2)
#Space Complexity : O(1)


#Better Approach
#Sorting the array and then checking for consecutive elements

def longestConsecutive(self, arr: list[int]) -> int:
        arr.sort()
        count = 1
        maxi = 0
        lastsmall = float('-inf')
        for i in range(len(arr)):
            if arr[i]-1 == lastsmall:
                count += 1
                lastsmall = arr[i]
            elif arr[i] != lastsmall:
                lastsmall = arr[i]
                count = 1
            maxi = max(count,maxi)
        return maxi
nums = list(map(int,input().split(",")))
print(longestConsecutive(nums)) #input : 100,4,200,1,3,2
#Output : 4

#Time Complexity : O(nlogn)
#Space Complexity : O(1)

#Optimized Approach
#Using Hashing

def longestConsecutive(self, arr: list[int]) -> int:
        numset = set(arr)
        count = 0
        maxi = 0
        for i in range(len(arr)):
            if arr[i]-1 not in numset:
                count = 1
                x = arr[i]
                while (x+1) in numset:
                    count += 1
                    x += 1
            maxi = max(maxi,count)
        return maxi
nums = list(map(int,input().split(",")))
print(longestConsecutive(nums)) #input : 100,4,200,1,3,2
#Output : 4

#Time Complexity : O(n)
#Space Complexity : O(n)


    