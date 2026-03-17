1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def invertTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: Optional[TreeNode]
12        """
13
14        if root is None:
15            return 
16        root.left, root.right = root.right, root.left
17        self.invertTree(root.left)
18        self.invertTree(root.right)
19        return root
20
21        # swap left and right of the children
22        # go down the left branch further 
23        # perform the swap on the left again
24        # repeat until it is none, esentially stopping the recutsion further on the left branch 
25        # when its none then it moves onto the next line which is the right branch 
26        # and does the same thing as the left side 
27        