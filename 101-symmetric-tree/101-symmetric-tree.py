# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return
        else:
            return self.ismirror(root.left,root.right)
            
            
    def ismirror(self,l,r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False

        return l.val == r.val and self.ismirror(l.left,r.right) and self.ismirror(l.right,r.left)  