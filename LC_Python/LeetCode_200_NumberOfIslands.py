import collections

def numIslands(grid):
    if len(grid) < 1: # Base case: check if edge case that we are given nothing
        return 0

    ROWS, COLS = len(grid), len(grid[0]) # dimensions of grid (usual set up for matrix problems)
    visited = set() # check if we have already seen the island

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
            grid[r][c] == "0" or (r, c) in visited): # Base case: Check if we are out bounds OR water OR that we have run DFS before on it
            return

        visited.add((r,c)) # Mark as seen. Helps not re-run DFS and not double count islands
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                result += 1
                dfs(r, c) # We have the start of an island, DFS through it to mark all points that are apart of that 1 island
    return result

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


# ------------ BFS ------------ #

def numIslands(grid):
  ROWS, COLS = len(grid), len(grid[0])
  res = 0

  def helper(i, j):
    q = collections.deque([(i, j)])
    while q:
      r, c = q.popleft()
      directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      for x, y in directions:
        rx, cy = r + x, c + y
        if rx >= 0 and cy >= 0 and rx < ROWS and cy < COLS and grid[rx][cy] == '1':
          grid[rx][cy] = '0' # IMPORTANT that the change is made here for every valid add-on to curr island
          q.append((rx, cy))

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == '1':
        helper(r, c)
        res += 1
  return res