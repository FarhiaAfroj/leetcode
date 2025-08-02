#include <vector>
using namespace std;

/*
 * Returns all possible combinations of k numbers chosen from the range [1, n].
 * Time complexity is proportional to the number of combinations × k (to copy paths).
 * Space complexity (output + recursion stack) is O(C(n,k) + k).
 */
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> path;
        backtrack(1, n, k, path, ans);
        return ans;
    }

private:
    void backtrack(int start, int n, int k,
                   vector<int>& path, vector<vector<int>>& ans) {
        if ((int)path.size() == k) {
            ans.push_back(path);
            return;
        }
        for (int x = start; x <= n; ++x) {
            path.push_back(x);
            backtrack(x + 1, n, k, path, ans);
            path.pop_back();
        }
    }
};
