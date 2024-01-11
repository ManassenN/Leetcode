# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first_tree_leafs,second_tree_leafs=[],[]
        def dfs(node,leafs):
            if not node:
                return 

            # This row means that we are on a leaf
            if not node.left and not node.right:
                leafs.append(node.val)
            
            dfs(node.left,leafs)
            dfs(node.right,leafs)

            return leafs
        first_tree_leafs = dfs(root1,[])
        second_tree_leafs = dfs(root2,[])

        if first_tree_leafs == second_tree_leafs:
            return True
        else:
            return False        