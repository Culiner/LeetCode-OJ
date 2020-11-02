#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 无限次交易O(n^2)
        # sell = [0]
        # for i in range(1, len(prices)):
        #     max_value = sell[i-1]
        #     for j in range(len(sell)-1):
        #         max_value = max(max_value, sell[j]+(prices[i]-min(prices[j+1:i])))
        #     sell.append(max_value)
        # return sell[-1]
        
        # O(n^2)
        # sell = [[0, 0, 0] for i in range(len(prices))]
        # for i in range(1, len(prices)):
        #     for j in range(i):
        #         diff = prices[i]-min(prices[j:i])
        #         sell[i][1] = max(sell[i][1], sell[j][0]+diff, sell[j][1])
        #         sell[i][2] = max(sell[i][2], sell[j][1]+diff, sell[j][2])
        # return max(sell[-1][0], sell[-1][1], sell[-1][2])
        
        sell = [0]
        now_min = prices[0]
        for i in range(1, len(prices)):
            sell.append(max(prices[i]-now_min, 0))
            now_min = min(now_min, prices[i])
        money_max = sell[-1]
        now_max = 0
        diff_max = 0
        for i in range(len(prices)-1, 0, -1):
            diff_max = max(diff_max, now_max-prices[i])
            money_max = max(money_max, diff_max+sell[i-1], sell[i-1])
            now_max = max(now_max, prices[i])
        return money_max