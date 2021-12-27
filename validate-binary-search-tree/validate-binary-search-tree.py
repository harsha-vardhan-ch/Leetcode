 

INT_MAX = 4294967296
INT_MIN = -4294967296
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(root,mini,maxi):
            #print(root.val)
            if root is None:
                return True
            if root.val<=mini or root.val>=maxi:
                return False
            return (isvalid(root.left,mini,root.val) and isvalid(root.right,root.val,maxi))
        #print("Here")
        return isvalid(root,INT_MIN,INT_MAX)
        
        