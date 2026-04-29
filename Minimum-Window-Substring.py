1class Solution(object):
2    def minWindow(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: str
7        """
8        # handle edge cases
9
10        characters_t = {}
11        characters_window = {}
12
13        for ch in t:
14            characters_t[ch] = characters_t.get(ch, 0) + 1
15
16        want = 0
17        need = len(characters_t)
18
19        # looking for min so start at biggest possible value
20        best_result_len = float("infinity")
21        best_result = [-1, -1]
22        len_window = 0
23
24        lp = 0
25
26        for r in range(len(s)):
27            characters_window[s[r]] = characters_window.get(s[r], 0) + 1
28
29            if s[r] in characters_t and characters_window[s[r]] == characters_t[s[r]]:
30                want += 1
31
32            while want == need:
33                if (r - lp + 1) < best_result_len:
34                    best_result = [lp, r]
35                    best_result_len = r - lp + 1
36                
37                # remove from left side
38                characters_window[s[lp]] -= 1
39                if s[lp] in characters_t and characters_window[s[lp]] < characters_t[s[lp]]:
40                    want -= 1
41
42                lp += 1
43
44        start, end = best_result
45
46        if best_result_len != float("infinity"):
47            return s[start:end+1]
48        else:
49            return ""
50                
51
52        
53
54        