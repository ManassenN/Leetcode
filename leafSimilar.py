def leafSimilar(root1,root2):
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