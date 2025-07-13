# Problem Description:
# You are given an array nums containing n distinct numbers. These n numbers are taken from the range [0, n]. Your task is to find and return the only number in the range [0, n] that is missing from the array.
# Example:
# If n = 3 and nums = [3, 0, 1]:
# The numbers in the range [0, n] are 0, 1, 2, 3.
# The number 2 is missing from nums.
# Input Format:
# The input will consist of two lines:The first line contains an integer n, representing the number of elements in the array nums. The second line contains n space-separated integers, representing the elements of nums.
# Output Format:
# Print a single integer, the missing number.
# Constraints:
# All numbers in nums are unique.
# Exactly one number from the range [0, n] is missing.
# Test Cases:
# Test Case 1: Basic Example
# Input:3

# 3 0 1
# Expected Output: 2

# method 1:
n = int(input())
numArr = list(map(int, input().split()))
checkArr = [False]*(n+1)

for i in range(n):
    checkArr[numArr[i]] = True

index = checkArr.index(False)
print(index)

# method 2:
n = int(input())
numArr = list(map(int, input().split()))
sum = n*(n+1)//2

arrSum = sum(numArr)
missing_number = sum - arrSum
print(missing_number)
