"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

**STUDY** = this took me longer than it should have to get an eglent solution
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        start = prev = ListNode(1)
        prev.next = head
        
        while prev.next and prev.next.next:
            # swap
            slow, fast = prev.next, prev.next.next
            prev.next, slow.next, fast.next = fast, fast.next, slow
            prev = prev.next.next
            
        return start.next
