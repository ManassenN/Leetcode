# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        pass






def tree_to_undirected_graph(root,graph = None):
    if graph is None:
        graph = {}

    if root not in graph:
        graph[root] = set()

    if node.left.val          