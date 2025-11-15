#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        vector<int> result;
        
        for (int i = 0; i <= n - k; i++) {
           
            map<int, int> freq;
            for (int j = i; j < i + k; j++) {
                freq[nums[j]]++;
            }
           
            vector<pair<int, int>> elements;
            for (auto& p : freq) {
                elements.push_back(p);
            }
          
            sort(elements.begin(), elements.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
                if (a.second != b.second) {
                    return a.second > b.second;
                }
                return a.first > b.first;
            });
          
            int sum = 0;
            int count = min(x, (int)elements.size());
            for (int idx = 0; idx < count; idx++) {
   
                sum += elements[idx].first * elements[idx].second;
            }
            
            result.push_back(sum);
        }
        
        return result;
    }
};