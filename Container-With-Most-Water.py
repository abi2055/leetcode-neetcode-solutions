1class Solution(object):
2    def maxArea(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        r = len(height)-1
8        l = 0
9        largest = 0
10        shortest_bar = 0
11
12        while r > l:
13            shortest_bar = min(height[r], height[l])
14            area = shortest_bar*(r-l)
15            largest = max(area, largest)
16            if height[r] > height[l]:
17                l = l + 1
18            elif height[r] < height[l]:
19                r = r - 1
20            else:
21                r = r - 1
22        
23        return largest
24        