class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> graph;
        for (auto& ticket : tickets) {
            graph[ticket[0]].insert(ticket[1]);
        }
        
        vector<string> itinerary;
        stack<string> st;
        st.push("JFK");
        
        while (!st.empty()) {
            string curr = st.top();
            if (graph[curr].empty()) {
                itinerary.push_back(curr);
                st.pop();
            } else {
                auto next = graph[curr].begin();
                st.push(*next);
                graph[curr].erase(next);
            }
        }
        
        reverse(itinerary.begin(), itinerary.end());
        return itinerary;
    }
};