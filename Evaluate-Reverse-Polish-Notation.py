1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        # operation tokens are not pushed to the stack
4        # numbers are pushed to the stack in order 
5
6        stack_numbers = []
7        calculation = 0 
8
9        for token in tokens:
10            if token == "/" or token == "+" or token == "-" or token == "*":
11                num_a = int(stack_numbers.pop())
12                num_b = int(stack_numbers.pop())
13                if token == "+":
14                    calculation = num_b + num_a
15                elif token == "-":
16                    calculation = num_b - num_a
17                elif token == "*":
18                    calculation = num_b * num_a
19                elif token == "/":
20                    calculation = num_b / num_a
21                
22                stack_numbers.append(calculation)
23
24            else:
25                stack_numbers.append(token)
26
27        return int(stack_numbers.pop())