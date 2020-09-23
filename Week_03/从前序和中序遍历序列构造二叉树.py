class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree(preorder[1+index:],inorder[index+1:])
        return root
