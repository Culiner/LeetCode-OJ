#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    # max_value = 9999999

    # def deep(self, clips, T, used, n):
    #     if n == len(clips):
    #         return self.max_value
    #     result = self.max_value
    #     for i in range(len(clips)):
    #         if (i in used and used[i]) or clips[i][1] < T or clips[i][0] >= T:
    #             continue
            
    #         if clips[i][0] == 0:
    #             result = n+1
    #             break

    #         used[i] = True
    #         result = min(result, self.deep(clips, clips[i][0], used, n+1))
    #         used[i] = False
    #     return result

    # def videoStitching(self, clips: List[List[int]], T: int) -> int:
    #     result = self.deep(clips, T, {}, 0)
    #     if result == self.max_value:
    #         return -1
    #     return result

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [101] * T
        for i in range(1, T+1):
            for single in clips:
                if single[0] <= i <= single[1]:
                    dp[i] = min(dp[i], dp[single[0]] + 1)
        return dp[T] if dp[T]!=101 else -1