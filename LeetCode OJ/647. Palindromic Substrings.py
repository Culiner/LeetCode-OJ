#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        memo = {}
        cnt = 0
        for s_len in range(len(s)):
            for i in range(len(s)-s_len):
                if i not in memo:
                    memo[i] = {}
                if s_len == 0:
                    memo[i][i] = True
                    cnt += 1
                elif s[i] == s[i+s_len] and (s_len == 1 or memo[i+1][i+s_len-1]):
                    memo[i][i+s_len] = True
                    cnt += 1
                else:
                    memo[i][i+s_len] = False
        return cnt