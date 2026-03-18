1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def diameterOfBinaryTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        # go all the way down left
14        # go all the way down right
15        # add both sides lengths together 
16        if root is None:
17            return 0 
18
19        self.diameter = 0
20
21        def dfs(node):
22            if node is None:
23                return 0
24
25            left = dfs(node.left)
26            right = dfs(node.right)
27
28            self.diameter = max(self.diameter, left + right)
29            return 1 + max(left, right)
30        
31        dfs(root)
32        return self.diameter