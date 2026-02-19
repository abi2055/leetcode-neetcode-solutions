1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7
8        rightp = 0
9        leftp = 0
10        store = 0
11
12        for i in range(len(nums)):
13            if (nums[i] != 0):
14                rightp = i 
15                store = nums[rightp]
16                nums[rightp] = nums[leftp]
17                nums[leftp] = store
18                leftp = leftp + 1
19
20        return nums
21        
22
23                    
24    
25    # find a zero
26    # find the next element
27    # allow a swap of those two elements and continue along 
28
29        