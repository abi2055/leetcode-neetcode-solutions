1class Solution(object):
2    def maxSubArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        # brute force is O(n^2) or O(n^3)
8        # greedy is alot faster
9
10        max_subarray = nums[0]
11        current_total = 0
12        
13        for num in nums:
14            if current_total < 0:
15                current_total = 0
16            current_total += num
17            max_subarray = max(max_subarray, current_total)
18        
19        return max_subarray
20