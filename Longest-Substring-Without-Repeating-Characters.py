1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        
8        substring_set = set()
9        lp = 0
10        how_long = 0
11
12        for r in range(len(s)):
13            while s[r] in substring_set:
14                substring_set.remove(s[lp])
15                lp += 1
16            substring_set.add(s[r])
17            how_long = max(how_long, len(substring_set))
18        
19        return how_long
20
21        