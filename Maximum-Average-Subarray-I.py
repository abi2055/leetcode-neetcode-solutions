1class Solution(object):
2    def findMaxAverage(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: float
7        """
8        
9        # looking at continous elements and summing them up together 
10        # this looks like a basic sliding window problem 
11        # from the 4 summed up from the arry we are finding the max average
12        # initially looking at the problem it is brute forcable by using two for loops
13        # one for loop will iterate through length of nums - k position and the second will sum everything together
14        # however the time complexity is at minimum O(N^2) not even looking at conditional statements which is quite inefficient 
15
16        # first sum the initial k values of the array
17        summ = 0
18        for i in range(k):
19            summ += nums[i]
20
21        # answer will be the initial sum at the start
22        ans = float(summ)/k
23        avg = 0
24
25        for i in range(len(nums)-k):
26            summ = summ - nums[i]
27            summ = summ + nums[i+k]
28            avg = float(summ)/k
29            if (avg > ans):
30                ans = avg
31
32        return ans
33
34        # sliding window 
35        