class Solution(object):
    def countIslands(self, grid, k):
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] <= 0:
                return 0
            val = grid[r][c]
            grid[r][c] = 0  # Mark as visited
            return val + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and dfs(r, c) % k == 0:
                    ans += 1
        return ans
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        