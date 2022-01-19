# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        if root:
            r=r+self.postorderTraversal(root.left)
            r=r+self.postorderTraversal(root.right)
            r=r+[root.val]
        return r