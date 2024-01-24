from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def dfs(node,path,count):
            if not node:
                if check_permutation_palindrome(path):
                    count +=1
                return count

            else:
                path.append(node.val)
                dfs(node.left,path,count)
                dfs(node.left,path,count)
        return dfs(root,[],0)

def check_permutation_palindrome(lst):
        # Count the occurrences of each element on the list.
            lst = Counter(lst)

        # Track the number of elements with odd counts
            odd_count = 0

            for count in lst.values():
                if count % 2 != 0:
                    odd_count += 1

            if odd_count <= 1:
                return True
            else:
                return False 
                           