
class Solution {
public:
    // Check if repeated string (seq * k) is a subsequence of s
    bool isKSubsequence(const string& seq, const string& s, int k) {
        int i = 0, repeat = 0;
        for (char c : s) {
            if (c == seq[i]) {
                i++;
                if (i == seq.size()) {
                    i = 0;
                    repeat++;
                    if (repeat == k) return true;
                }
            }
        }
        return false;
    }

    string longestSubsequenceRepeatedK(string s, int k) {
        unordered_map<char, int> freq;
        for (char c : s) freq[c]++;
        
        // Keep only characters that occur at least k times
        string chars = "";
        for (auto& [ch, f] : freq) {
            if (f >= k) chars += ch;
        }

        sort(chars.rbegin(), chars.rend()); // Try bigger letters first

        queue<string> q;
        q.push("");
        string result = "";

        while (!q.empty()) {
            int size = q.size();
            vector<string> nextLevel;
            for (int i = 0; i < size; ++i) {
                string curr = q.front();
                q.pop();
                for (char c : chars) {
                    string next = curr + c;
                    if (isKSubsequence(next, s, k)) {
                        nextLevel.push_back(next);
                        if (next.size() > result.size() || 
                           (next.size() == result.size() && next > result)) {
                            result = next;
                        }
                    }
                }
            }
            for (string& str : nextLevel) {
                if (str.size() < 7) {  // limit depth to avoid TLE
                    q.push(str);
                }
            }
        }

        return result;
    }
};
