class Solution:
    def isValidBST(self, root):
        def isValid(root,lower,upper):
            if not root:
                return True
            if lower<root.val<upper:
                return isValid(root.left,lower,root.val) and isValid(root.right,root.val,upper)
            else:
                return False
        inf = float('inf')
        return isValid(root,-inf,inf)