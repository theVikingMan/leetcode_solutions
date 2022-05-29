import collections

def maxDepth(root):
    # base case if root is none -> see if its a max
    if not root:
        return 0
    return 1 +  max(self.maxDepth(root.left), self.maxDepth(root.right))

# --------------- Iteratively --------------- #

def maxDepth(root):
  if not root:
    return 0
  q = collections.deque([root])
  maxD = 0
  while q:
    maxD += 1
    for _ in range(len(q)):
      node = q.popleft()
      if node.right:
        q.append(node.right)
      if node.left:
        q.append(node.left)
  return maxD