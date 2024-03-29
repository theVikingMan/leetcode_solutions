def maxAreaOfIsland(grid):
    ROWS, COLS = len(grid), len(grid[0]) # set rows and cols variables
    res = 0 # result variable to return with max area
    visited = set() # track all seen coordinates so we dont run BFS on a previous ran one

    def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
            return 0 # Checking if in bounds, seen or not an island

        visited.add((r,c)) # mark it as seen, will NOT unmark as we need to track which
                           # coordinates have been looked at. Clean up would break this.

        # If the point satisfies all the cases to be a part of the answer, +1 to area
        # Then search if the island continues in all directions
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for r in range(ROWS):
        for c in range(COLS):
            res = max(dfs(r, c), res)
    return res

print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0,0],
                       [0,1,0,0,1,1,0,0,1,0,1,0,0],
                       [0,1,0,0,1,1,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,0,0,0,0,0,0,1,1,0,0,0,0]]))


# ------------ Iterative DFS (stack) ----------- #

# def maxAreaOfIsland(grid):
#   ROWS, COLS = len(grid), len(grid[0])
#   seen = set()
#   res = 0

#   def helper(r, c):
#     stack = [(r, c)]
#     size = 1
#     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     while stack:
#       r, c = stack.pop()

#       for x, y in directions:
#         rx, cy = r+x, c+y
#         if 0 <= rx < ROWS and 0 <= cy < COLS and (rx, cy) not in seen and grid[rx][cy] == 1:
#           stack.append((rx, cy))
#           seen.add((rx, cy))
#           size += 1
#     return size

#   for r in range(ROWS):
#     for c in range(COLS):
#       if (r, c) not in seen and grid[r][c] == 1:
#         seen.add((r, c))
#         res = max(res, helper(r, c))
#   return res