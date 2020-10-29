#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect_single(self, now_node, bro_node):
        if now_node is None:
            return
        now_node.next = bro_node
        if now_node is not None:
            self.connect_single(now_node.left, now_node.right)
        if bro_node is not None:
            self.connect_single(now_node.right, bro_node.left)
            self.connect_single(bro_node.left, bro_node.right)

    def connect(self, root: 'Node') -> 'Node':
        self.connect_single(root, None)
        return root