1class Solution(object):
2    def countGoodSubstrings(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        
8        # using sliding window to go over every 3 letter substring throw them all in a list
9        # iterate through that list and use set check if its 3 long again each time 
10
11        pointer_start = 0
12        pointer_end = 0
13        number_good = 0
14
15        for i in range(len(s)):
16            pointer_start = i
17            pointer_end = pointer_start + 2
18            if (pointer_end != len(s)):
19                if (len(set(s[pointer_start:pointer_end+1])) == 3):
20                    number_good += 1
21            else:
22                break
23
24        return number_good
25        
26        
27