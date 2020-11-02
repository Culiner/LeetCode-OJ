#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def reset(self, n):
        return 1 if n == 0 else 0

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            length = len(A[i])
            n = int(length/2+1) if length%2==1 else int(length/2)
            for j in range(n):
                tmp = A[i][j]
                A[i][j] = self.reset(A[i][length-j-1])
                A[i][length-j-1] = self.reset(tmp)
        return A