import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        # Base case: if we are given no root at the beginning
        # OR that we ahve reached the end
        if not root:
            return
        # holder for one of the nodes as we will modify it but need a version that is
        # unmodified
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Time: O(n) --> have to visit all nodes once
# Space: O(n) --> recursive call stack

# --------------- Iteratively --------------- #

def invertTree(root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left # switch node pointers
            queue.append(node.left) # add nodes to be evaulated
            queue.append(node.right) # add nodes to be evaulated
    return root

# Time: O(n) --> have to visit all nodes once
# Space: O(n) --> size of the stack which would contain all nodes