class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        breakpoint = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                breakpoint = i-1
                break
        else:
            return nums.reverse()
        for i in range(len(nums)-1,breakpoint,-1):
            if nums[i]>nums[breakpoint]:
                nums[breakpoint] ,nums[i] = nums[i],nums[breakpoint]
                break
        i,j = breakpoint+1,len(nums)-1
        while(i<j):
            nums[i] , nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        return nums

    
#Input: nums = [1,2,3]
#Output: [1,3,2]
#Time Complexity: O(n)
#Space Complexity: O(1)


        


        