1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSubtree(self, root, subRoot):
9        """
10        :type root: Optional[TreeNode]
11        :type subRoot: Optional[TreeNode]
12        :rtype: bool
13        """
14
15            # once you find a potential match then go all the way down
16        
17        def checkSubtree(node, subNode):
18            if not node and not subNode:
19                return True
20            # condition goes all the way to the end meaning both nodes end
21            # at the same time
22
23            if not node or not subNode:
24                return False
25            # goes all the way to end on one tree but not the other
26
27            if node.val != subNode.val:
28                return False
29            # values do not match
30
31            return checkSubtree(node.left, subNode.left) and checkSubtree(node.right, subNode.right)
32
33        def search(node):
34            if not node:
35                return False
36            # no starting point found
37
38            if checkSubtree(node, subRoot):
39                return True
40            
41            # found a starting point
42            
43            return search(node.left) or search(node.right)
44
45        is_same = search(root)
46        return is_same
47
48
49        