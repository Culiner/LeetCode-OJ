#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == j == 0:
                    dp[i][j] = 1
                    continue
                total = 0
                if i > 0:
                    total += dp[i-1][j]
                if j > 0:
                    total += dp[i][j-1]
                dp[i][j] = total
        return dp[-1][-1]
