#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

# class Solution:
#     min_total = -1

#     def step_next(self, now_m, now_n, grid, now_total, m, n):
#         now_total += grid[now_m][now_n]
#         if self.min_total != -1 and now_total >= self.min_total:
#             return
#         if now_m == m - 1 and now_n == n - 1:
#             if self.min_total == -1 or self.min_total > now_total:
#                 self.min_total = now_total
#             return
#         if now_m == m - 1:
#             self.step_next(now_m, now_n+1, grid, now_total, m, n)
#         elif now_n == n - 1:
#             self.step_next(now_m+1, now_n, grid, now_total, m, n)
#         elif grid[now_m+1][now_n] > grid[now_m][now_n+1]:
#             self.step_next(now_m, now_n+1, grid, now_total, m, n)
#             self.step_next(now_m+1, now_n, grid, now_total, m, n)
#         else:
#             self.step_next(now_m+1, now_n, grid, now_total, m, n)
#             self.step_next(now_m, now_n+1, grid, now_total, m, n)

#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         if m == 0:
#             return 0
#         n = len(grid[0])
#         self.step_next(0, 0, grid, 0, m, n)
#         return self.min_total

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    result[i][j] = grid[i][j]
                elif i == 0:
                    result[i][j] = result[i][j-1] + grid[i][j]
                elif j == 0:
                    result[i][j] = result[i-1][j] + grid[i][j]
                else:
                    result[i][j] = min(result[i][j-1], result[i-1][j]) + grid[i][j]
        return result[m-1][n-1]