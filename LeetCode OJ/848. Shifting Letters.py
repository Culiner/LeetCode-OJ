#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        total = 0
        for i in range(len(shifts)-1, -1, -1):
            tmp = shifts[i]
            shifts[i] = (shifts[i] + total) % 26
            total = (tmp + total) % 26
        result = ''
        for i in range(len(S)):
            result += chr((ord(S[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
        return result

# print(Solution().shiftingLetters("abc", [3,5,9]))