class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
    
        vector<vector<int>> grid(m, vector<int>(n, 0));
     
        for (auto& w : walls) {
            grid[w[0]][w[1]] = 2;
        }
        
        for (auto& g : guards) {
            grid[g[0]][g[1]] = 3;
        }
      
        for (int r = 0; r < m; r++) {
            bool guarded = false;
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 3) {
                    guarded = true;
                } else if (grid[r][c] == 2) {
                    guarded = false;
                } else if (guarded) {
                    grid[r][c] = 1;
                }
            }
        }
    
        for (int r = 0; r < m; r++) {
            bool guarded = false;
            for (int c = n-1; c >= 0; c--) {
                if (grid[r][c] == 3) {
                    guarded = true;
                } else if (grid[r][c] == 2) {
                    guarded = false;
                } else if (guarded) {
                    grid[r][c] = 1;
                }
            }
        }
      
        for (int c = 0; c < n; c++) {
            bool guarded = false;
            for (int r = 0; r < m; r++) {
                if (grid[r][c] == 3) {
                    guarded = true;
                } else if (grid[r][c] == 2) {
                    guarded = false;
                } else if (guarded) {
                    grid[r][c] = 1;
                }
            }
        }
     
        for (int c = 0; c < n; c++) {
            bool guarded = false;
            for (int r = m-1; r >= 0; r--) {
                if (grid[r][c] == 3) {
                    guarded = true;
                } else if (grid[r][c] == 2) {
                    guarded = false;
                } else if (guarded) {
                    grid[r][c] = 1;
                }
            }
        }
     
        int count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) count++;
            }
        }
        return count;
    }
};