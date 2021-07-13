#include <iostream>
#include <set>
#include <vector>
using namespace std;

int solution(vector<int> nums) {
    size_t pickup = nums.size() / 2;
    set<int> phoneketmon(nums.cbegin(), nums.cend());
    return min(phoneketmon.size(), pickup);
}

int main() {
    cout << "답 : " << solution({3, 1, 2, 3}) << endl;
    cout << "답 : " << solution({3, 3, 3, 2, 2, 4}) << endl;
    cout << "답 : " << solution({3, 3, 3, 2, 2, 2}) << endl;
}