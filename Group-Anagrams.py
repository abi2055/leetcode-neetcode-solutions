1class Solution(object):
2    def groupAnagrams(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: List[List[str]]
6        """
7
8        keys = []      
9        buckets = []   
10
11        for word in strs:
12            sorted_word = ''.join(sorted(word))  
13
14            if sorted_word in keys:               
15                i = keys.index(sorted_word)     
16                buckets[i].append(word)
17            else:
18                keys.append(sorted_word)          
19                buckets.append([word])    
20        
21        return buckets
22        