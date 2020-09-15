class Solution:
    def levelOrder(self, root):
        if not root: return []
        result = []
        stack = [root]
        while stack:
            length = len(stack)
            temp = []
            for _ in range(length):
                node = stack.pop(0)
                temp.append(node.val)
                for son in node.children:
                    stack.append(son)
            result.append(temp)
        return result