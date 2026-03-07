1class Solution(object):
2    def trap(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        
8        # min(maxL, maxR) - height if position i
9
10        max_left = 0
11        max_right = 0
12        max_left_store = []
13        max_right_store = []
14        water_pos_i = 0
15        res = 0
16        
17        for i in range(len(height)):
18            max_left = max(max_left, height[i])
19            max_right = max(max_right, height[len(height) - 1 - i])
20            max_left_store.append(max_left)
21            max_right_store.append(max_right)
22
23        max_right_store.reverse()
24
25        for i in range(len(height)):
26            water_pos_i = min(max_left_store[i], max_right_store[i]) - height[i]
27            if water_pos_i > 0:
28                res += water_pos_i
29            
30        return res
31        