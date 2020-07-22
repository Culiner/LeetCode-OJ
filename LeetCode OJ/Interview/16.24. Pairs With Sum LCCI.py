#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        use_map = {}
        for i in nums:
            if i not in use_map:
                use_map[i] = 0
            use_map[i] += 1
        result = []
        for i in nums:
            if (i == target-i and use_map[i] >= 2) or (i != target-i and use_map[i] > 0 and target-i in use_map and use_map[target-i] > 0):
                result.append([i, target-i])
                use_map[i] -= 1
                use_map[target-i] -= 1
        return result