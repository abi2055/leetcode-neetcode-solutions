1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        if not matrix:
9            return False
10
11        rows = len(matrix)
12        cols = len(matrix[0])
13        start = 0
14        end = (rows*cols)-1
15
16        while start <= end:
17            mid = (start+end)//2
18            row = mid // cols
19            col = mid % cols
20            val = matrix[row][col]
21
22            if val == target:
23                return True
24            elif val < target:
25                start = mid + 1
26            else:
27                end = mid - 1
28
29        return False
30
31