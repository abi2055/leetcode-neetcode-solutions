1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSameTree(self, p, q):
9        """
10        :type p: Optional[TreeNode]
11        :type q: Optional[TreeNode]
12        :rtype: bool
13        """
14        def dfs(nodep, nodeq):
15            if not nodep and not nodeq:
16                return True
17
18            if nodep is None or nodeq is None:
19                return False
20            
21            if nodep.val != nodeq.val:
22                return False
23            
24            return dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right)
25
26        is_same = dfs(q, p)
27        return is_same
28            
29        