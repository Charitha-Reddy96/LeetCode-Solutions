class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        new_arr = [0]*len(arr)
        pos , neg = 0,1
        for i in range(len(arr)):
            if arr[i]>0:
                new_arr[pos] = arr[i]
                pos += 2
            else:
                new_arr[neg] = arr[i]
                neg += 2
        return new_arr
    
#Time Complexity: O(n)
#Space Complexity: O(n)
# This code rearranges the elements of an array such that positive and negative numbers alternate.
# It uses two pointers to fill the new array with positive numbers at even indices and negative numbers at odd indices.
# The time complexity is O(n) because it iterates through the array once, and the space complexity is O(n) due to the new array created.
