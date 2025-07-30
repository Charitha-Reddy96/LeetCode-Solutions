class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mpp = defaultdict(int)
        preSum = 0
        cnt = 0
        mpp[0] = 1 
        for i in range(n):
            preSum += arr[i]
            remove = preSum - k
            cnt += mpp[remove]
            mpp[preSum] += 1
        return cnt
    
#Time Complexity: O(n)
#Space Complexity: O(n)


#Using Normal Dictonary 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = sum = 0
        n =  len(nums)
        map = {}
        map[0] = 1 
        for i in range(n):
            sum += nums[i]
            rem = sum - k 
            if rem in map:
                count += map[rem]
            if sum in map:
                map[sum] += 1
            if sum not in map:
                map[sum] = 1
        return count
    
#Time Complexity: O(n)
#Space Complexity: O(n)