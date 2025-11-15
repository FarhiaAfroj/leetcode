class Solution {
public:
    int maxDistance(string s, int k) {
        int n = s.length();
        
        vector<int> e(n+1,0), w(n+1,0), n_(n+1,0), s_(n+1,0);
        
        for (int i = 0; i < n; i++) {
            e[i+1] = e[i] + (s[i] == 'E');
            w[i+1] = w[i] + (s[i] == 'W');
            n_[i+1] = n_[i] + (s[i] == 'N');
            s_[i+1] = s_[i] + (s[i] == 'S');
        }
        
        int ans = 0;
        for (int t = 1; t <= n; t++) {
            int x0 = e[t] - w[t];
            int y0 = n_[t] - s_[t];
           
            int bad = w[t] + s_[t];
            int val = x0 + y0 + 2 * min(k, bad);
            ans = max(ans, val);
         
            bad = w[t] + n_[t];
            val = x0 - y0 + 2 * min(k, bad);
            ans = max(ans, val);
          
            bad = e[t] + s_[t];
            val = -x0 + y0 + 2 * min(k, bad);
            ans = max(ans, val);
           
            bad = e[t] + n_[t];
            val = -x0 - y0 + 2 * min(k, bad);
            ans = max(ans, val);
        }
        
        return ans;
    }
};