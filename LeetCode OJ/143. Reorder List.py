#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        node_slow = head
        node_fast = head
        while node_fast.next is not None and node_fast.next.next is not None:
            node_slow = node_slow.next
            node_fast = node_fast.next.next
        tmp = node_slow
        node_slow = node_slow.next
        tmp.next = None

        node_slow_pre = None
        while node_slow is not None:
            tmp = node_slow.next
            node_slow.next = node_slow_pre
            node_slow_pre = node_slow
            node_slow = tmp
        
        now_node1 = head
        now_node2 = node_slow_pre
        while now_node2 is not None:
            now_node1_next = now_node1.next
            now_node2_next = now_node2.next
            now_node1.next = now_node2
            now_node2.next = now_node1_next
            now_node1 = now_node1_next
            now_node2 = now_node2_next