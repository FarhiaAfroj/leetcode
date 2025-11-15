class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.length();
        
        vector<int> zero_pos;
        for (int i = 0; i < n; i++) {
            if (s[i] == '0') {
                zero_pos.push_back(i);
            }
        }
        
        int count = 0;
        int m = zero_pos.size();
        
        long long ones_segment = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                ones_segment++;
            } else {
                count += ones_segment * (ones_segment + 1) / 2;
                ones_segment = 0;
            }
        }
        count += ones_segment * (ones_segment + 1) / 2;
        
        for (int z = 1; z <= min(200, m); z++) {
            int min_len = z * z + z;
            if (min_len > n) continue;
            
            for (int i = 0; i + z - 1 < m; i++) {
                int first_zero = zero_pos[i];
                int last_zero = zero_pos[i + z - 1];
                
                int start_min = (i == 0) ? 0 : (zero_pos[i - 1] + 1);
                int start_max = first_zero;
                int end_min = last_zero;
                int end_max = (i + z == m) ? (n - 1) : (zero_pos[i + z] - 1);
              
                for (int start = start_min; start <= start_max; start++) {
                    int min_end = max(end_min, start + min_len - 1);
                    if (min_end <= end_max) {
                        count += (end_max - min_end + 1);
                    }
                }
            }
        }
        
        return count;
    }
};