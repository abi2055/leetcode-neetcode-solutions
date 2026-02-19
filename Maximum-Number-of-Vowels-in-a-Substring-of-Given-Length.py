1class Solution(object):
2    def maxVowels(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: int
7        """
8
9        # classic sliding window problem
10        # get the original substring k and store it in a variable
11        # run a for loop to substract and add an additional character from the substring
12        # check how many vowels are in it each time, its possible to use ASCII here to optimize 
13
14        initial_substring = s[0:3]
15        sub2 = ""
16        vowel_count = 0 
17        ans = 0
18        max_count = 0
19
20        for i in range(k):
21            if (s[i] in "aeiou" ):
22                vowel_count += 1
23
24        max_count = vowel_count
25
26        for i in range(k, len(s)):
27            if (s[i] in "aeiou"):
28                vowel_count += 1
29            if (s[i-k] in "aeiou"):
30                vowel_count -= 1
31            max_count = max(vowel_count, max_count)
32
33        return max_count
34            
35
36
37
38
39        