1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        # prefix and suffix calculation and mapping
8        # create 2 arrays prefix and suffix 
9        # for each number ignore the current value, take whatever comes before and whatever comes after 
10        # and multiply them 
11        # this question should be a hard...
12
13        prefix = [1] * len(nums)
14        # 1 since, 1 x anything is = anything
15        suffix = [1] * len(nums)
16        result = [1] * len(nums)
17 
18        for i in range(1, len(nums)):
19            prefix[i] = prefix[i - 1] * nums[i - 1]
20
21        for i in range(len(nums)-2, -1, -1):
22            suffix[i] = suffix[i + 1] * nums[i + 1]
23
24        for i in range(len(nums)):
25            result[i] = prefix[i]*suffix[i]
26
27        return result