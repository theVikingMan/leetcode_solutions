import collections

# ------ Post-Order ------ #

def postorderTraversal(self, root):
    res = []
    def bfs(node):
        if node:
            bfs(node.left)
            bfs(node.right)
            res.append(node.val)
    bfs(root)
    return res

# ------ Pre-Order ------ #

def preorderTraversal(self, root):
    output = []
    def dfs(node):
        if not node:
            return
        output.append(node.val)
        dfs(node.left)
        dfs(node.right)

# ------ In-Order ------ #

def preorderTraversal(self, root):
    output = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        output.append(node.val)
        dfs(node.right)

# ------ Level-Order ------ #

queue = collections.deque([root])
output = []

while queue:
    to_add = []
    for _ in range(len(queue)):
        node = queue.popleft()
        if node:
            to_add.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    if to_add:
        output.append(to_add)
return output


# ------ ZIGZAG ------ #

queue = collections.deque([root])
output = []

while queue:
    to_add = []
    for _ in range(len(queue)):
        node = queue.popleft()
        if node:
            to_add.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    if to_add:
        output.append(to_add if len(output) % 2 == 0 else to_add[::-1])
return output