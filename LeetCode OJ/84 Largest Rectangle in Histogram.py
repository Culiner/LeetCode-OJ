#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights : return 0
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result,h * w)
            stack.append(i)
        return result

print(Solution().largestRectangleArea([1,1]))