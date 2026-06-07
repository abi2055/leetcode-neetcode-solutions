1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11         # put values in an array and then reorder values
12
13        # store = []
14        # re_array = []
15        # current = head 
16         
17        # while current:
18        #     store.append(current.val)
19        #     current = current.next
20
21        # print(store)
22
23        # p1 = 0
24        # p2 = len(store) - 1
25
26        # while p2 > p1:
27        #     re_array.append(store[p1])
28        #     re_array.append(store[p2])
29        #     p1 += 1
30        #     p2 -= 1
31        
32        # print(re_array)
33
34        # start with fast and slow pointer 
35        # fast is x2 of slow
36        # then reverse the links of the lists, slow pointer is the end of list 1
37        # fast pointer is the end of list 2
38        # then merge the nodes in the reordered format 
39
40        fast = head
41        slow = head
42
43        while fast and fast.next:
44            slow = slow.next
45            fast = fast.next.next
46        # getting positions needed
47
48        # reverse the links of list 2 
49        list2 = slow.next 
50        # this is the head 
51        prev = None
52        slow.next = None
53        # with the reversion the head will reference null
54
55        while list2:
56            temp = list2.next
57            list2.next = prev
58            prev = list2
59            list2 = temp
60
61        # the merge
62        first_list = head
63        second_list = prev
64        while second_list:
65            temp1 = first_list.next
66            temp2 = second_list.next
67            first_list.next = second_list
68            second_list.next = temp1
69            first_list = temp1
70            second_list = temp2
71
72
73
74
75
76            
77
78
79
80