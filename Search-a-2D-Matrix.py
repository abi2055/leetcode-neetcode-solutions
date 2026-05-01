1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        # find the appropriate row
9        # do binary search on that appropriate row 
10
11        rows = len(matrix)
12        cols = len(matrix[0])
13        
14        top_row = 0
15        bottom_row = rows - 1
16
17        while top_row <= bottom_row:
18            mid_row = (top_row + bottom_row) // 2
19            if target > matrix[mid_row][cols-1]:
20                top_row = mid_row + 1
21            elif target < matrix[mid_row][0]:
22                bottom_row = mid_row - 1
23            else:
24                break
25            
26        if top_row > bottom_row:
27            return False
28
29        mid_row = (top_row + bottom_row) // 2
30        left = 0
31        right = cols - 1
32
33        while left <= right:
34            mid = (left + right) // 2
35            if target > matrix[mid_row][mid]:
36                left = mid + 1
37            elif target < matrix[mid_row][mid]:
38                right = mid - 1
39            else:
40                return True
41            
42        return False
43