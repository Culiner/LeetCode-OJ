#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        if matrix[0] is str :
            result = now = 0 
            for i in range(len(matrix)):
                now = now + 1  if matrix[i] == '1' else 0
                result = max(result,now)
            return result

        heights = [0] * (len(matrix[0]) + 1)
        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    result = max(result,h * w)
                stack.append(i)

        return result

print(Solution().maximalRectangle(["1","0","1","1"]))