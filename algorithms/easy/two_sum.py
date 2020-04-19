from typing import List

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