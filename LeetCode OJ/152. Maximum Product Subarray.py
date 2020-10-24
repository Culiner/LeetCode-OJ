#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_dp = [nums[0]]
        max_dp = [nums[0]]
        max_value = nums[0]
        for i in range(1, len(nums)):
            num1 = min_dp[i-1]*nums[i]
            num2 = max_dp[i-1]*nums[i]
            num3 = nums[i]
            min_dp.append(min(num1, num2, num3)) 
            max_dp.append(max(num1, num2, num3)) 
            max_value = max(max_value, max_dp[i])
        return max_value