# Link: https://leetcode.com/problems/number-of-islands/description/

from collections import deque

def numIslands(grid):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        q = deque()
        grid[r][c] = '0'
        q.append((r, c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'):
                    continue
                q.append((nr, nc))
                grid[nr][nc] = '0'

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                bfs(r, c)
                islands += 1

    return islands


print(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
