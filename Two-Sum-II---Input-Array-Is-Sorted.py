1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        l = 0
9        r = len(numbers)-1
10        summ = 0
11
12        while l < r:
13            if numbers[r] + numbers[l] == target:
14                break
15            elif numbers[r] + numbers[l] > target:
16                r -= 1
17            elif numbers[r] + numbers[l] < target:
18                l += 1
19        
20        return [l+1, r+1]