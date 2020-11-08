#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                res_sum = 0
                if i > 0:
                    res_sum += dp[i-1][j]
                if j > 0:
                    res_sum += dp[i][j-1]
                dp[i][j] = res_sum
        return dp[-1][-1]