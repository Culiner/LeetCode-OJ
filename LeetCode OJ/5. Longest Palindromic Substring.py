#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_str = s[0]
        memo = {}
        for s_len in range(len(s)):
            for i in range(len(s)-s_len):
                if i not in memo:
                    memo[i] = {}
                if s_len == 0:
                    memo[i][i] = True
                elif s[i] == s[i+s_len] and (s_len == 1 or memo[i+1][i+s_len-1]):
                    max_str = s[i:i+s_len+1]
                    memo[i][i+s_len] = True
                else:
                    memo[i][i+s_len] = False
        return max_str

# print(Solution().longestPalindrome("cbbd"))
