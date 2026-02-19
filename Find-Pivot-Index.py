1class Solution(object):
2    def pivotIndex(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n = len(nums)
8        prefix = [0]*(n+1)
9        for i in range(n):
10            prefix[i+1] = prefix[i] + nums[i]
11
12        for i in range(n):
13            if prefix[i] == prefix[n] - prefix[i+1]:
14                return i
15        return -1