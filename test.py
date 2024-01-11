class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_undirected_graph(root, graph=None):
    if graph is None:
        graph = {}

    if root not in graph:
        graph[root] = set()

    if root.left or root.right:
        children = [child for child in [root.left, root.right] if child is not None]

        for child in children:
            graph[root].add(child)
            if child not in graph:
                graph[child] = set()
            graph[child].add(root)

            tree_to_undirected_graph(child, graph)

# Example usage:
# Construct a tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Convert the tree to an undirected graph
undirected_graph = {}
tree_to_undirected_graph(root, undirected_graph)

# Print the undirected graph
for node, neighbors in undirected_graph.items():
    print(f"{node.val} -> {[neighbor.val for neighbor in neighbors]}")
