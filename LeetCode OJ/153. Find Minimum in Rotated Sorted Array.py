#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        search_left = 0
        search_right = len(nums) - 1
        base = nums[0]
        while True:
            i = int((search_left+search_right)/2)
            if nums[i] >= base and nums[i+1] < base:
                return nums[i+1]
            elif nums[i] > base and nums[i+1] > base:
                search_left = i
            elif nums[i] < base and nums[i+1] < base:
                search_right = i
