1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7                # you go through each element once
8        # and you essentially just twosum the remaining ones 
9        # sort them first
10        
11        res_list = []
12        nums.sort()
13
14        for index, value in enumerate(nums):
15            if index > 0 and value == nums[index-1]:
16                continue 
17            # if you encounter a duplicate thats not the first value in the array
18            # skip since we already looked at that permutation basically
19
20            left = 1 + index
21            right = len(nums)-1
22
23            while left < right:
24                if value + nums[left] + nums[right] > 0:
25                    right -= 1
26                elif value + nums[left] + nums[right] < 0:
27                    left += 1
28                else:
29                    res_list.append([value, nums[left], nums[right]])
30                    left += 1
31                    while nums[left] == nums[left - 1] and left < right:
32                        left += 1
33        
34        return res_list