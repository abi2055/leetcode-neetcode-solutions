1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums) - 1
5
6        while l <= r:
7            mid = (l + r) // 2
8            
9            if nums[mid] == target:
10                return mid
11            
12            if nums[l] <= nums[mid]:
13                # this is the range of values in the left portion
14                # if the target is inside we keep the left side
15                if nums[l] <= target < nums[mid]:
16                    r = mid - 1
17                # discard left
18                else:
19                    l = mid + 1
20            else:
21                # this is the range of values in the right portion
22                # if the target is inside the range we keep the right side
23                if nums[mid] < target <= nums[r]:
24                    l = mid + 1
25                else:
26                    r = mid - 1
27
28        return -1
29