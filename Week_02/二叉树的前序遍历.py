class Solution:
    def preorderTraversal(self, root):
        result = []
        def pre(cur):
            if cur:
                result.append(cur.val)
                pre(cur.left)
                pre(cur.right)
        pre(root)
        return result