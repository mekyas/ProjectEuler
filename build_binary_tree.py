from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, postorder):
            if not(len(inorder)>0 and len(postorder)>0):
                return None
            else:
                root_val = postorder[-1]
                root = TreeNode(root_val)
                idx = inorder.index(root_val)
                root.left = build(inorder[0:idx], [i for i in postorder if i in inorder[0:idx]])
                root.right = build(inorder[idx+1:], [i for i in postorder if i in inorder[idx+1:]])
                return root
        return build(inorder, postorder)

a = buildTree([9,3,15,20,7],[9,15,7,20,3])
print(a)