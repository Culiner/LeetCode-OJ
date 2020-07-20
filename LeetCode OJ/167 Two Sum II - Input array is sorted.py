#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            if numbers[i] > target:
                break
            for j in range(i+1, len(numbers)):
                tmp = numbers[i]+numbers[j]
                if tmp > target:
                    break
                elif tmp == target:
                    return [i+1, j+1]

tmp = Solution()
print(tmp.twoSum([2, 7, 11, 15], 9))