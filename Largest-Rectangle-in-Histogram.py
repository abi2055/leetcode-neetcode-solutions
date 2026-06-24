1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        largest_result = 0
4        stack = []
5
6        for i, h in enumerate(heights):
7            start_index = i
8            while stack and stack[-1][1] > h:
9                # the top of the stack's height is greater than current height
10                index, height = stack.pop()
11                largest_result = max(largest_result, (i - index) * height)
12                # the smallest height would be limiting
13                start_index = index
14            stack.append((start_index, h))
15
16        for i, h in stack:
17            largest_result = max(largest_result, (len(heights) - i) * h)
18
19        return largest_result
20
21