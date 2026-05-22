1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        # formula aka time = (target - position) / speed
4
5        # list comprehension
6        combined = [[pos, speed] for pos, speed in zip(position, speed)]
7
8        # sorting for traversal purposes
9        combined = sorted(combined)
10
11        stack = []
12
13        for pos, speed in combined[::-1]:
14            stack.append((target - pos) / speed)
15            if len(stack) >= 2 and stack[-2] >= stack[-1]:
16                stack.pop()
17
18        return len(stack)
19
20
21        