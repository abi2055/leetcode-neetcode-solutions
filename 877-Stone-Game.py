class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # think of it as a knapsack problem 
        # optimization by checking both options 
        # the dp formula: dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j - 1])
        # rather than computing the max we compute the edge
        # the winning edge is the winning result 

        n = len(piles)

        # knapsack 2d matrix shorthand
        knapsack = [[0] * n for _ in range(n)]

        for i in range(n):
            knapsack[i][i] = piles[i]
            # on the diagonal 

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                knapsack[i][j] = max(piles[i] - knapsack[i+1][j], piles[j] - knapsack[i][j - 1])

        return knapsack[0][n-1] > 0
        # return true if the last column of the first row has a greater edge than 0