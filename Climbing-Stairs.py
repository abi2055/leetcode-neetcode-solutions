1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        # two methods
8        # with memory of O(n) create an array to store previous values in the state
9        # or completely forget about the array and just compute with a temp var which is O(1)
10
11        # Array solution 
12        # if n <= 2:
13        #     return n
14
15        # state_store = [0] * (n+1)
16        # state_store[1] = 1
17        # state_store[2] = 2
18
19        # for i in range(3, n+1):
20        #     state_store[i] = state_store[i-1] + state_store[i-2]
21
22        # return state_store[n]
23
24        # Second Solution O(1)
25        if n <= 2:
26            return n
27
28        two_before = 1
29        one_before = 2
30
31        for i in range(3, n+1):
32            temp = two_before + one_before
33            two_before = one_before
34            one_before = temp
35        
36        return one_before
37
38        
39
40
41