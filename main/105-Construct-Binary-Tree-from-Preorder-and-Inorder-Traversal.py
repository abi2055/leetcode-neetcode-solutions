# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
           # preorder traversal: root, left, right nodes

        # inorder traversal: left, root, right nodes
        # inorder returns ordered nodes from smallest to largest values
        # which is why its useful in a BST

        # postorder traversal: left, right, root nodes

        # the idea  
        # there will be two partitions coming from the inorder traversal
        # one from the left of root (the left subtree)
        # one from right of root (the right subtree)
        # each node you traverse you create 

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        # start of tree
        mid = inorder.index(preorder[0])
        # getting the index value of the middle root value
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root




        