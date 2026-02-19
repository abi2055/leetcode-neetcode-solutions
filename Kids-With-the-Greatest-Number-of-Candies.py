1class Solution(object):
2    def kidsWithCandies(self, candies, extraCandies):
3        largest = 0
4        bools = []
5        for c in candies:
6            if c > largest:
7                largest = c
8
9        for i in range(len(candies)):
10            if (candies[i] + extraCandies >= largest):
11                bools.append(True)
12            else:
13                bools.append(False)
14
15        return bools
16        