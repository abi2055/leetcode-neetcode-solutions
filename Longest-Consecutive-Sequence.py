1class Solution(object):
2    def longestConsecutive(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        # If we only care about what comes before and after
8        # not the actual number itself 
9
10        converted = set(nums)
11        longest = 0
12
13        for num in converted:
14            if (num - 1) not in converted:
15            # trying to find numbers that start the sequence
16                length = 0
17                while (num + length) in converted:
18                    # checking if numbers can be chained in a series
19                    length += 1
20                longest = max(length, longest)
21
22        return longest