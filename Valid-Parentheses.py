1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7
8        # A strategy where the closing and opening parantheses are next to eachother
9        
10        stack = []
11        bracket_list = {')': '(', '}': '{', ']': '['}
12
13        for ch in s: 
14            if ch in bracket_list:
15                if stack and stack[-1] == bracket_list.get(ch):
16                # without popping, verify non-empty stack
17                    stack.pop()
18                else:
19                    return False
20            else:
21                stack.append(ch)
22
23        if stack:
24            return False
25        else:
26            return True
27        