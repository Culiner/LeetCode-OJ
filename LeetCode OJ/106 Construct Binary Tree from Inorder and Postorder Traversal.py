#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTreeUtil(self, inorder, postorder, inOrderMap, pStart, pEnd, iStart, iEnd):
        if pStart > pEnd or iStart > iEnd : return None
        node = TreeNode(postorder[pEnd])
        index = inOrderMap[node.val]
        node.left = self.buildTreeUtil(inorder, postorder, inOrderMap, pStart, pStart + index - iStart - 1, iStart, index - 1)
        node.right = self.buildTreeUtil(inorder, postorder, inOrderMap, pStart + index - iStart, pEnd - 1, index + 1, iEnd)
        return node

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inOrderMap = {inorder[i]:i for i in xrange(len(inorder))}
        return self.buildTreeUtil(inorder,postorder,inOrderMap,0,len(postorder) - 1,0,len(inorder) - 1)

tmp = Solution().buildTree([4,2,5,1,3,6],[4,5,2,6,3,1])
print tmp