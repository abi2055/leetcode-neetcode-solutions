1class Solution(object):
2    def generateParenthesis(self, n):
3        """
4        :type n: int
5        :rtype: List[str]
6        """
7        
8        # conditions 
9        # open_par < n
10        # closed_par < open_par 
11
12        results = []
13        open_number = 0
14        closed_number = 0
15
16        def backtrack(current, open_number, closed_number):
17            if len(current) == 2 * n:
18                results.append(current)
19                return 
20
21            if open_number < n:
22                backtrack(current + "(", open_number + 1, closed_number)
23            
24            if closed_number < open_number:
25                backtrack(current + ")", open_number, closed_number + 1)
26            
27        backtrack("", 0, 0)
28        return results