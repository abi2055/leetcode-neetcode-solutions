# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs 
        # remember conditions for bts

        def dfs(node, highest, lowest):
            if not node:
                return True

            if not (node.val < highest and node.val > lowest):
                return False
            
            return dfs(node.left, node.val, lowest) and dfs(node.right, highest, node.val)

        return dfs(root, float('inf'), float('-inf'))

