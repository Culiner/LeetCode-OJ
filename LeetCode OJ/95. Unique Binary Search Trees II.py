#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate_trees_deep(self, nums) -> List[TreeNode]:
        if len(nums) == 1:
            return [TreeNode(nums[0], None, None)]
        result = []
        for i in range(len(nums)):
            left = [None]
            if i != 0:
                left = self.generate_trees_deep(nums[:i])
            right = [None]
            if i != len(nums)-1:
                right = self.generate_trees_deep(nums[i+1:])
            for single_left in left:
                for single_right in right:
                    result.append(TreeNode(nums[i], single_left, single_right))
        return result

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate_trees_deep(range(1, n+1))