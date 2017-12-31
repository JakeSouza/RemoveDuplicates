'''
Created on Dec 30, 2017

@author: Jake
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 1
        count = len(nums) - 1
        for x in range(count):
            if(nums[first] == nums[second]):
                nums.remove(nums[first])
                count -= 1
            else:
                first += 1
                second += 1
        return len(nums)