1class Solution(object):
2    def numIslands(self, grid):
3        """
4        :type grid: List[List[str]]
5        :rtype: int
6        """
7        # bfs traversal 
8        # check neighbors each iteration 
9        # when all surrounding adjacent neighbors (not diagonal) are 0
10        # update the count
11
12        # this will represents all the nodes visited as a global var
13        visited = set()
14        islands = 0
15
16        def bfs(row, column):
17            queue = collections.deque()
18            queue.append((row, column))
19            visited.add((row, column))
20
21            while queue:
22                row, column = queue.popleft()
23
24                # must check each direction for bfs for adjacent nodes
25                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
26
27                # loop through the directions
28                for drow, dcol in directions:
29                    # checks 
30                    if (0 <= row + drow < len(grid) and 
31                        0 <= column + dcol < len(grid[0]) and 
32                            grid[row + drow][column + dcol] == "1" and
33                                (row + drow, column + dcol) not in visited):
34                                    queue.append((row + drow, column + dcol))
35                                    visited.add((row + drow, column + dcol))
36
37        for row in range(len(grid)):
38            for col in range(len(grid[0])):
39
40                # only bfs is a 1 ignore all the 0s
41                if grid[row][col] == "1" and (row, col) not in visited:
42                    # basically performing bfs on the graph node
43                    bfs(row, col)
44                    islands += 1
45                
46        return islands
47        