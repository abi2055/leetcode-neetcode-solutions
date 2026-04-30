1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        # edge cases 
14
15        # have a running count of left and right
16        # if left and right differ by max 1 then return true
17        self.balanced = True
18
19        def dfs(node):
20            if node is None:
21                return 0
22
23            left = dfs(node.left)
24            right = dfs(node.right)
25
26            if abs(right - left) > 1:
27                self.balanced = False
28
29            return 1 + max(left, right)
30
31        dfs(root)
32
33        return self.balanced
34        