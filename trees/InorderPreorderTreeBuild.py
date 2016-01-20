class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


 
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    
    def buildTree(self, preorder, inorder):
        if not inorder: 
            return None 
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
        return root





def postorder(preorder, inorder):
  if len(preorder) <= 1:
    return preorder
  v = preorder[0]
  preorder = preorder[1:]
  pivot = inorder.find(v)
  left = inorder[0:pivot]
  right = inorder[pivot+1:]
  return postorder(preorder[:len(left)], left) + postorder(preorder[len(left):], right) + v

print postorder('421356', '123456')

