#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell = [0]
        # for i in range(1, len(prices)):
        #     max_res = 0
        #     for j in range(i):
        #         min_val = min(prices[j:i])
        #         max_res = max(max_res, sell[j], sell[j]+prices[i]-min_val)
        #     sell.append(max_res)
        # return sell[-1]
        sell = [[0, -prices[0]]]+[[0,0]]*(len(prices)-1)
        for i in range(1, len(prices)):
            sell[i][0] = max(sell[i-1][0], sell[i-1][1]+prices[i])
            sell[i][1] = max(sell[i-1][1], sell[i-1][0]-prices[i])
        return sell[-1][0]
