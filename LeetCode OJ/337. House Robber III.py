#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def rob(self, now_node: TreeNode, memo={}) -> int:
#         if now_node in memo:
#             return memo[now_node]
#         if now_node is None:
#             return 0
#         if now_node.left is None and now_node.right is None:
#             return now_node.val
#         # if not choose now node
#         val_child = self.rob(now_node.left) + self.rob(now_node.right)
#         # if choose now node
#         val_self = now_node.val
#         if now_node.left is not None:
#             val_self += self.rob(now_node.left.left) + self.rob(now_node.left.right)
#         if now_node.right is not None:
#             val_self += self.rob(now_node.right.left) + self.rob(now_node.right.right)
#         result = max(val_child, val_self)
#         memo[now_node] = result
#         return result 

class Solution:
    def rob_deep(self, now_node: TreeNode):
        if now_node is None:
            return [0, 0]
        result = [0, 0]
        left = self.rob_deep(now_node.left)
        right = self.rob_deep(now_node.right)
        result[0] = max(left[0], left[1]) + max(right[0], right[1])
        result[1] = left[0] + right[0] + now_node.val
        return result

    def rob(self, now_node: TreeNode) -> int:
        result = self.rob_deep(now_node)
        return max(result[0], result[1])