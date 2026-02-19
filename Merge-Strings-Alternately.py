1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        complete_word = []
9        count = 0
10        shorter = ""
11        longer = ""
12
13        if len(word1) > len(word2):
14            shorter = word2
15            longer = word1
16        else:
17            shorter = word1
18            longer = word2
19
20        for i in range(len(shorter)):
21            complete_word.append(word1[i])
22            complete_word.append(word2[i])
23
24        complete_word.append(longer[len(shorter):len(longer)])
25
26        answer = "".join(complete_word)
27
28        return answer
29        