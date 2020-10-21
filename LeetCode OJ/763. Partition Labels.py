#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def find_max(self, S: str, single: str):
        for i in range(len(S)-1, -1, -1):
            if S[i] == single:
                return i
        return 0

    def partitionLabels(self, S: str) -> List[int]:
        result = []
        now_max = -1
        now_length = 0
        for i in range(len(S)):
            now_max = max(self.find_max(S, S[i]), now_max)
            now_length += 1
            if i == now_max:
                result.append(now_length)
                now_length = 0
                continue
        return result
            