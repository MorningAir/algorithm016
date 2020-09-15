class Solution:
    def preorder(self, root):
        result = []
        stack = [root]
        while stack:
            a = stack.pop()
            result.append(a.val)
            temp = []
            for i in a.children:
                temp.append(i)
            stack.extend([temp][::-1])
        return result
