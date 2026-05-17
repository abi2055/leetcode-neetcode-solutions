1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        # keep temperatures in stack
4        # we pop until element has bigger than amount
5        # we dont care if they are lost during the pop
6        results = [0] * len(temperatures)
7        stack = []
8
9        for index, temp in enumerate(temperatures):
10            while stack and temp > stack[-1][1]:
11                # top of the stack is -1 to peek
12                stack_index, stack_temp = stack.pop()
13                results[stack_index] = index - stack_index
14                # i - stack_index basically gives us the 
15                # number of days in the future
16
17            stack.append([index, temp])
18
19        return results
20
21
22
23
24