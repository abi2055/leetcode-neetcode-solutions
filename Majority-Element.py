1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        
8        # frequency counting problem 
9
10        nums_frequency = {}
11
12        for num in nums:
13            nums_frequency[num] = nums_frequency.get(num, 0) + 1 
14
15        common = max(nums_frequency.values())
16
17
18        if (common > (len(nums)/2)):
19            return max(nums_frequency, key=nums_frequency.get)