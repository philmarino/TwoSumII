def twoSum(numbers, target):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return []

# Example 1:
# Input: 
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: 
numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: 
numbers = [-1,0]
target = -1
print(twoSum(numbers, target))
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 