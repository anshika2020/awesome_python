class NumberOfIsland:
    def numIslands(self, grid):
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt += 1
                    self.helper(grid, r, c)
        return cnt
    def helper(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        self.helper(grid, r + 1, c)
        self.helper(grid, r - 1, c)
        self.helper(grid, r, c + 1)
        self.helper(grid, r, c - 1)
    # Example usage:
if __name__=="__main__":
    island = NumberOfIsland();
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
print(island.numIslands(grid))
