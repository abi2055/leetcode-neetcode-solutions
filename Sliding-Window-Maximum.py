1class Solution(object):
2    def maxSlidingWindow(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8
9        # 1. brute force 
10
11        # lp = 0
12        # rp = k
13        # res = []
14
15        # for i in range(0, len(nums)-k+1):
16        #     largest = float("-inf")
17        #     for c in range (lp, rp):
18        #         if nums[c] > largest:
19        #             largest = max(largest, nums[c])
20
21        #     print("left pointer: ", lp)
22        #     print("right pointer: ", rp)
23            
24        #     res.append(largest)
25        #     lp += 1
26        #     rp += 1
27            
28        # return res
29
30        # 2. heap solution 
31
32        max_store = []
33        results = []
34        left_pointer = 0
35
36        for index, value in enumerate(nums):
37            heapq.heappush(max_store, (-value, index))
38            # storing both the index of that value and the max of that value
39            # python sorts by the first index 
40            
41            # index = right pointer
42            if index >= k - 1:
43                left_pointer = index - k + 1
44
45                while max_store[0][1] < left_pointer:
46                    heapq.heappop(max_store)
47
48                results.append(-max_store[0][0])
49        
50        return results
51        