1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseList(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12
13        # Iterative Solution
14        current = head
15        prev = None
16
17        while current:
18            # the next node after the current head 
19            up_next = current.next
20            # first iteration references None, second iteration references the one before
21            current.next = prev
22            # the previous moves to the current node
23            prev = current
24            # current moves forward one 
25            current = up_next
26
27        return prev 
28        