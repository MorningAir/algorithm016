class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        elif root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif not right:
            return left
        elif not left:
            return right
