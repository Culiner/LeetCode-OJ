#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while True:
            if i+nums[i] >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            max_i = i
            max_step = 0
            for j in range(i, i+nums[i]+1):
                tmp_max = j + nums[j]
                if tmp_max > max_step:
                    max_i = j
                    max_step = tmp_max
            if max_i == i:
                return False
            i = max_i
                