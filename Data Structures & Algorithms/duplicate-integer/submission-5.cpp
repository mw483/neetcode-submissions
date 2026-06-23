#include <list>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> seen;
        for (int i=0; i < std::size(nums); i++) {
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.insert(nums[i]);
        }
        return false;
    }
};