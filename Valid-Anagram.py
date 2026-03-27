1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        # different solutions 
9
10        # for loop that stores letters in dict 
11        # o(len(s) + len(t)) -> O(n)
12
13        # or just sort both and compare
14        # if sorted(s) == sorted(t):
15        #     return True
16
17        # return False
18
19        # Less Pythonic but still optimal
20
21        counter_dict = {}
22
23        if len(s) != len(t):
24            return False
25
26        for i in range(len(s)):
27            counter_dict[s[i]] = counter_dict.get(s[i], 0) + 1
28            counter_dict[t[i]] = counter_dict.get(t[i], 0) - 1
29
30        for value in counter_dict.values():
31            if value != 0:
32                return False
33        
34        return True
35