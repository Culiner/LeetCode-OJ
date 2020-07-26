#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def generate_list(self, nums_map, now_list, result, last_num):
        for i in nums_map:
            if nums_map[i] > 0:
                now_list.append(i)
                if last_num == 1:
                    result.append(now_list[:])
                else:
                    nums_map[i] -= 1
                    self.generate_list(nums_map, now_list, result, last_num-1)
                    nums_map[i] += 1
                now_list.pop()
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_map = {}
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 0
            nums_map[i] += 1
        self.generate_list(nums_map, [], result, len(nums))
        return result
    