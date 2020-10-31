#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, level, val, result):
        if root is None:
            return False
        if root.val == val or self.dfs(root.left, level+1, val, result) or self.dfs(root.right, level+1, val, result):
            result[root] = level
            return True
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_result = {}
        self.dfs(root, 0, p.val, p_result)
        q_result = {}
        self.dfs(root, 0, q.val, q_result)
        
        parent_val = 0
        parent_level = -1
        for single in p_result:
            if single in q_result and p_result[single] > parent_level:
                parent_level = p_result[single]
                parent_val = single
        return parent_val