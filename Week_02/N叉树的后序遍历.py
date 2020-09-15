class Solution:
    def postorder(self, root):
        result = []
        def solve(cur):
            if cur:
                for i in cur.children:
                    solve(i)
                result.append(cur.val)
        solve(root)
        return result