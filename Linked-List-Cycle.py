1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def hasCycle(self, head):
9        """
10        :type head: ListNode
11        :rtype: bool
12        """
13         # hashset method
14        current = head
15
16        visited = set()
17
18        while current:
19            if current in visited:
20                return True
21            visited.add(current)
22            current = current.next
23        
24        return False
25        