#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, now_val):
        if root is None:
            return 0
        now_val = now_val*10+root.val
        if root.left is None and root.right is None:
            return now_val
        return self.dfs(root.left, now_val)+self.dfs(root.right, now_val)

    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)