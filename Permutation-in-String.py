1class Solution(object):
2    def checkInclusion(self, s1, s2):
3        """
4        :type s1: str
5        :type s2: str
6        :rtype: bool
7        """
8        # put everything s1 in a hashmap
9        # put the sliding window of s2 in a hashmap and compare
10
11        s1_count = {}
12        s2_count = {} 
13
14        p1 = 0
15        p2 = len(s1)
16
17        window = 0
18
19        if len(s1) > len(s2):
20            return False
21
22        for i in range(len(s1)):
23            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
24            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
25
26        if s1_count == s2_count:
27            return True
28
29        window = len(s1)
30
31        for p2 in range(window, len(s2)):
32            s2_count[s2[p2]] = s2_count.get(s2[p2], 0) + 1
33            s2_count[s2[p1]] = s2_count.get(s2[p1], 0) - 1
34
35
36            if s2_count[s2[p1]] == 0:
37                del s2_count[s2[p1]]
38
39            p1 += 1 
40
41            if s1_count == s2_count:
42                return True
43
44        return False
45
46