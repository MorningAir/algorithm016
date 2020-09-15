class Solution:
    def inorderTraversal(self, root):
        result = []
        def solve(cur):
            if cur:
                solve(cur.left)
                result.append(cur.val)
                solve(cur.right)
        solve(root)
        return result