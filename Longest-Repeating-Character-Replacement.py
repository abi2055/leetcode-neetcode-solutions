1class Solution(object):
2    def characterReplacement(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: int
7        """
8        frequency_count = {}
9        window = 0
10        largest_window = 0
11
12        p1 = 0
13        # p2 = 0
14
15        most_frequent = 0
16
17        # attempt 1
18        # for i in range(len(s)):
19        #     for value in frequency_count.values():
20        #         most_frequent = max(value, most_frequent)
21            
22        #     if window - most_frequent <= k:
23        #         frequency_count[s[p2]] = frequency_count.get(s[p2], 0) + 1
24        #         p2 += 1 
25        #     else:
26        #         frequency_count[s[p1]] = frequency_count.get(s[p1], 0) - 1
27        #         p1 += 1
28
29        #     window = p2 - p1
30
31        #     largest_window = max(window, largest_window)
32
33        # return largest_window
34
35        for p2 in range(len(s)):
36            frequency_count[s[p2]] = frequency_count.get(s[p2], 0) + 1
37            most_frequent = max(most_frequent, frequency_count.get(s[p2]))
38
39            window = p2 - p1 + 1
40
41            while window - most_frequent > k:
42                frequency_count[s[p1]] -= 1
43                p1 += 1
44                window = p2 - p1 + 1
45            
46            largest_window = max(window, largest_window)
47            
48        return largest_window
49
50        