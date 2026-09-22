#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // This is our "notebook". 
        // It stores data in pairs: {number, position}
        unordered_map<int, int> notebook;
        
        for (int i = 0; i < nums.size(); ++i) {
            
            // The number we are currently looking at
            int current_person = nums[i];
            
            // The number we need to find to hit our target
            int needed_person = target - current_person;
            
            // Step 1: Check the notebook. 
            // Have we already written down the needed person?
            if (notebook.find(needed_person) != notebook.end()) {
                
                // Step 2: We found a match! 
                // Return their position (from the notebook) and our current position (i)
                return {notebook[needed_person], i};
            }
            
            // Step 3: If they aren't in the notebook yet, write down the 
            // current person and their position for the future.
            notebook[current_person] = i;
        }
        
        // If no match is found (though the problem guarantees there is one)
        return {};
    }
};