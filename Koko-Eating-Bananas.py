1class Solution(object):
2    def minEatingSpeed(self, piles, h):
3        """
4        :type piles: List[int]
5        :type h: int
6        :rtype: int
7        """
8        # Calculate each potentially eating rate in a for loop
9        
10        largest_k = 0
11        for i in range(len(piles)):
12            largest_k = max(largest_k, piles[i])
13        
14        smallest_k = 1
15        result = 0
16
17        while smallest_k <= largest_k:
18            mid = (smallest_k + largest_k) // 2
19            sum_of_hours = 0
20            for i in range(len(piles)):
21                sum_of_hours += math.ceil(piles[i] + mid - 1) // mid
22            if sum_of_hours > h:
23                smallest_k = mid + 1
24            else:
25                result = mid
26                largest_k = mid - 1
27
28        return result
29
30
31
32