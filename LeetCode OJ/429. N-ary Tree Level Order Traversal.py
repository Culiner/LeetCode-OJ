#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(now_node, level):
            if now_node == None:
                return
            if len(result)<level:
                result.append([])
            result[level-1].append(now_node.val)
            if now_node.children:
                for single in now_node.children:
                    dfs(single, level+1)

        result = []
        dfs(root, 1)
        return result