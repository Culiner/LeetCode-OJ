#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            dp.append([0 for i in range(len(triangle[i]))])
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])