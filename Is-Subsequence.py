1class Solution(object):
2    def isSubsequence(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        
9        str1P = 0
10        str2P = 0
11
12        while str1P < len(s) and str2P < len(t):
13            if s[str1P] == t[str2P]:
14                str1P += 1
15            str2P += 1
16        
17        if (str1P == len(s)):
18            return True
19        else:
20            return False
21