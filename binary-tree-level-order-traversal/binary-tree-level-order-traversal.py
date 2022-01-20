# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r=[]
        level=[root]
        while root and level:
            currnodes=[]
            nextlevel=[]
            for node in level:
                currnodes.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            r.append(currnodes)
            level=nextlevel
        return r
                
            