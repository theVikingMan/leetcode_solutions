def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word): # check if we have the word
            return True

        #check if the word that we are building is invalid
        if (r < 0 or c < 0 or r >= ROWS or
        c >= COLS or word[i] != board[r][c] or
        (r, c) in path):
            return False

        path.add((r, c)) # Mark letter is in our path
        # check all directions
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))

        path.remove((r, c)) # no longer checking that path
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))