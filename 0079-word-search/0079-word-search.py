class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])

        def dfs(i, j, idx):
            # If matched entire word
            if idx == len(word):
                return True
            # Check bounds or mismatch
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False

            # Mark visited
            temp = board[i][j]
            board[i][j] = "#"

            # Explore neighbors: up, right, down, left
            found = (
                dfs(i - 1, j, idx + 1) or
                dfs(i + 1, j, idx + 1) or
                dfs(i, j - 1, idx + 1) or
                dfs(i, j + 1, idx + 1)
            )

            board[i][j] = temp  # Unmark
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
