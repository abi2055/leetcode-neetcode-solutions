1class Solution(object):
2    def maxAreaOfIsland(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        # bfs traversal 
8        # check neighbors each iteration 
9        # when all surrounding adjacent neighbors (not diagonal) are 0
10        # update the count
11
12        # this will represents all the nodes visited as a global var
13        visited = set()
14        count = 0
15        max_area = 0
16
17        def bfs(row, column):
18            queue = collections.deque()
19            queue.append((row, column))
20            visited.add((row, column))
21            count = 1
22
23            while queue:
24                row, column = queue.popleft()
25
26                # must check each direction for bfs for adjacent nodes
27                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
28
29                # loop through the directions
30                for drow, dcol in directions:
31                    # checks 
32                    if (0 <= row + drow < len(grid) and 
33                        0 <= column + dcol < len(grid[0]) and 
34                            grid[row + drow][column + dcol] == 1 and
35                                (row + drow, column + dcol) not in visited):
36                                    queue.append((row + drow, column + dcol))
37                                    visited.add((row + drow, column + dcol))
38                                    count += 1
39            return count
40                    
41
42        for row in range(len(grid)):
43            for col in range(len(grid[0])):
44
45                # only bfs is a 1 ignore all the 0s
46                if grid[row][col] == 1 and (row, col) not in visited:
47                    # basically performing bfs on the graph node
48                    count = bfs(row, col)
49
50                max_area = max(max_area, count)
51                count = 0
52                
53        return max_area