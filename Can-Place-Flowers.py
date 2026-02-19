1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        """
4        :type flowerbed: List[int]
5        :type n: int
6        :rtype: bool
7        """
8
9        count = 0
10        length = len(flowerbed)
11
12        for i in range(length):
13            # Check if current spot is empty and its neighbors are also empty (or out of bounds)
14            if flowerbed[i] == 0:
15                left_empty = (i == 0 or flowerbed[i - 1] == 0)  # True if at index 0 or left is empty
16                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)  # True if at last index or right is empty
17
18                if left_empty and right_empty:
19                    flowerbed[i] = 1  # Plant a flower
20                    count += 1  # Increase count
21                    if count >= n:  # If we have placed enough, return True
22                        return True
23        
24        return count >= n  # Check if we have placed enough flowers
25