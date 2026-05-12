1class MinStack(object):
2
3    def __init__(self):
4        self.stack = []
5        self.min_value = []
6        
7    def push(self, val):
8        self.stack.append(val)
9        if not self.min_value:
10            self.min_value.append(val)
11        # first iteration
12        else:
13            current_minimum = self.min_value[-1]
14            self.min_value.append(min(current_minimum, val))
15
16
17    def pop(self):
18        if self.stack:
19            self.stack.pop()
20        if self.min_value:
21            self.min_value.pop()
22        
23    def top(self):
24        if self.stack:
25            return self.stack[-1]
26        else:
27            return 0
28        
29    def getMin(self):
30        return self.min_value[-1]
31