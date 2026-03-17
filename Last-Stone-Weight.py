1class Solution(object):
2    def lastStoneWeight(self, stones):
3        """
4        :type stones: List[int]
5        :rtype: int
6        """
7        
8        for i in range(len(stones)):
9            stones[i] = stones[i]*(-1)
10        # everything essentially needs to be reversed for a max heap
11        # the most negative value (would be the largest abs value)
12        # would sit at the top of the heap
13
14        heapq.heapify(stones)
15
16        while len(stones) > 1:
17            largest = heapq.heappop(stones)*(-1)
18            second = heapq.heappop(stones)*(-1)
19
20            if largest != second:
21                heapq.heappush(stones, -(largest - second))
22            else:
23                heapq.heappush(stones, 0)
24
25        return -heapq.heappop(stones)
26
27        