class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while(left<right):
                sum = nums[i]+nums[right]+nums[left]
                if sum == 0:
                    var = [nums[i],nums[left],nums[right]]
                    result.append(var)
                    left += 1
                    right -=1
                    while  left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right]== nums[right+1]:
                        right -= 1  
                elif sum>0:
                    right -= 1
                else:
                    left +=1      
        return result

# Time Complexity: O(n^2)
# Space Complexity: O(1) for the result list, O(n) for the input list
# Note: The input list is sorted, which takes O(n log n) time, but the main logic runs in O(n^2).