class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int totalTime = 0;
        int n = colors.size();
        
        int i = 0;
        while (i < n) {
            int j = i;
            int sum = 0, maxVal = 0;
           
            while (j < n && colors[j] == colors[i]) {
                sum += neededTime[j];
                maxVal = max(maxVal, neededTime[j]);
                j++;
            }
           
            if (j - i > 1) {
                totalTime += (sum - maxVal);
            }
            i = j;
        }
        
        return totalTime;
    }
};