#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def rob_line(self, nums: List[int]) -> int:
        max_selectd = [nums[0]]
        max_not_selectd = [0]
        for i in range(1, len(nums)):
            max_selectd.append(max_not_selectd[i-1]+nums[i])
            max_not_selectd.append(max(max_selectd[i-1], max_not_selectd[i-1]))
        return max(max(max_selectd), max(max_not_selectd))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[1:]), self.rob_line(nums[:len(nums)-1]))