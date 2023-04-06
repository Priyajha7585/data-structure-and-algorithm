# Given an array of N integers. Your task is to print the sum of all of the integers.
# Example 1:
# Input:
# 4
# 1 2 3 4
# Output:
# 10
# Example 2:
# Input:
# 6
# 5 8 3 10 22 45
# Output
# 93

def arraySum(arr):
    arrSum = 0
    for i in arr:
        arrSum = arrSum + i
    return arrSum
print(arraySum([1, 2, 3, 4]))
print(arraySum([5, 8, 3, 10, 22, 45]))