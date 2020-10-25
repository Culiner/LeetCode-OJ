#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    result = []

    def deep(self, candidates, target, now_list, now_line):
        if target < 0:
            return
        if target == 0:
            self.result.append([i for i in now_list])
        for candidate in candidates:
            if candidate < now_line:
                continue
            self.deep(candidates, target-candidate, [i for i in now_list]+[candidate], candidate)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.deep(candidates, target, [], 0)
        return self.result