#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for k in range(0, int(len(matrix)/2)):
            for i in range(k, n-k):
                tmp = matrix[k][i]
                matrix[k][i] = matrix[n-i][k]
                matrix[n-i][k] = matrix[n-k][n-i]
                matrix[n-k][n-i] = matrix[i][n-k]
                matrix[i][n-k] = tmp
            