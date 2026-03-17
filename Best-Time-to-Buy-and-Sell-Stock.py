1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7                # if you follow a two pointer approach
8        # pointer one on first element
9        # pointer two on the second element 
10        # check if pointer one, so on buy day 1, is greater than price on day 2
11        
12        left = 0
13        right = 1
14        cur_profit = 0
15        max_profit = 0
16
17        while right < len(prices):
18            # check profitablity
19            if prices[left] < prices[right]:
20                # we know theres a jump, so profit can be made
21                cur_profit = prices[right] - prices[left]
22                max_profit = max(max_profit, cur_profit)
23            else:
24                left = right
25            right += 1
26        
27        return max_profit