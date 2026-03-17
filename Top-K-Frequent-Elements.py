1class Solution(object):
2    def topKFrequent(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8
9        # create a frequency count dict/hashmap
10        # depending on k, get the largest counts in the dict
11
12        frequency_count = {}
13        top_nums = []
14
15        for num in nums:
16            if num in frequency_count:
17                frequency_count[num] += 1
18            else:
19                frequency_count[num] = 1
20        
21        for i in range(k):
22            max_key = max(frequency_count, key=frequency_count.get)
23            top_nums.append(max_key)
24            del frequency_count[max_key]
25
26        return top_nums
27        