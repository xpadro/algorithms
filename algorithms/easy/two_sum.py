from typing import List

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        
        for i in range(len(nums)):
            possible_num = target - nums[i]
            
            if possible_num in number_map:
                return [number_map[possible_num], i]
            else:
                number_map[nums[i]] = i
        
        return []