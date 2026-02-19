1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        
8        num_dict = {}
9
10        for num in nums:
11            num_dict[num] = num_dict.get(num, 0) + 1
12
13        if (max(num_dict.values()) >= 2):
14            return True
15        else:
16            return False 