#Brute Force Approach

def max_subarray_sum(arr):
    n= len(arr)
    sum = max =0
    for i in range(n):
        sum = 0 
        for j in range(i,n):
            sum += arr[j]
            if sum >max:
                max = sum
    return max
arr = [5,4,-1,7,8]
print(max_subarray_sum(arr))