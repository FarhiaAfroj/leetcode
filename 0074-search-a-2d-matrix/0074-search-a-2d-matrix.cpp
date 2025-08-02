#include <vector>
using std::vector;

class Solution {
public:
    bool searchMatrix(const vector<vector<int>>& A, int target) {
        int m = (int)A.size();
        if (m == 0) return false;
        int n = (int)A[0].size();
        if (n == 0) return false;

        int lo = 0, hi = m * n - 1;
        while (lo <= hi) {
            int mid = lo + ((hi - lo) >> 1);
            int row = mid / n;
            int col = mid % n;
            int val = A[row][col];
            if (val == target) return true;
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
};
