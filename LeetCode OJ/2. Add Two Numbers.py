#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_single(self, a, b, c):
        if a+b+c>=10:
            return a+b+c-10, 1
        else:
            return a+b+c, 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ex = 0
        root = ListNode(0)
        last_one = root
        while True:
            if l1 is None and l2 is None:
                if ex == 1:
                    last_one.next = ListNode(1)
                break
            else:
                v1 = 0
                if l1 is not None:
                    v1 = l1.val
                    l1 = l1.next
                v2 = 0
                if l2 is not None:
                    v2 = l2.val
                    l2 = l2.next
                val, ex = self.add_single(v1, v2, ex)
                last_one.next = ListNode(val)
                last_one = last_one.next
        return root.next