#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::vector<int> freq(26); // initialize frequency array
        if (s.length() != t.length()){
            return false;
        }
        
        for (int i = 0; i < s.length(); i++) {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }
        bool all_zeros = std::all_of(freq.begin(), freq.end(), [](int j) {return j == 0;});
        if (all_zeros == true) {
            return true;
        }
        else {
            return false;
        }
    }
};
