1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8         # simplest approach i can think of 
9        # keep an ongoing count 
10        # when you get to the ith index just do a reconnection with the node removed
11        # not the most clever solution that is with fast and slow pointers 
12
13        linked_len = 0
14        curr = head 
15        while curr:
16            linked_len += 1
17            curr = curr.next
18
19        target_index = linked_len - n
20
21        prev = None
22        curr = head 
23
24        for i in range(target_index):
25            print(i)
26            prev = curr
27            curr = curr.next
28
29        if prev is None:
30            return head.next
31        prev.next = curr.next
32
33        return head
34