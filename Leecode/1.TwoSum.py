'''
https://leetcode.com/problems/two-sum/description/
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsLenght = len(nums)
    for i in range(0,numsLenght):
            for j in range(i+1,numsLenght):
                if nums[i] + nums[j] == target:
                    return [i,j]

def twoSumUpgrade(nums, target):
    numsLenght = len(nums)
    searchNum = 0
    for i in range(0,numsLenght):
        searchNum = target - nums[i]
        if searchNum in nums:
            if nums.index(searchNum) != i:
                return [i,nums.index(searchNum)]

def twoSumAdvance(nums, target):
    print(nums)
    hash={}
    for i in range(len(nums)):
        hash[nums[i]] = i
    print(hash)
    for i in range(len(nums)):
        searchNum = target - nums[i ]
        if searchNum in hash and hash[searchNum] != i:
            return [i,hash[searchNum]]

# Check 
print(twoSum([2,9,5,5],10))
print(twoSumUpgrade([2,9,5,5],10))
print(twoSumAdvance([2,9,5,5],10))

'''
What I studied:
1. Using hash to find index of item
2. Using if i in <List>: to check item in List
3. List.Index(<item_value>) : return FIRST index of this item
'''