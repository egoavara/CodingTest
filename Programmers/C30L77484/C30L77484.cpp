#include <iostream>
#include <algorithm>
#include <array>
#include <set>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    array<int, 7> mapping{6, 6, 5, 4, 3, 2, 1};
    vector<int> answer;
    set<int> win(win_nums.cbegin(), win_nums.cend());
    auto matched = count_if(lottos.begin(), lottos.end(), [&](auto e) mutable {
        return win.find(e) != win.cend();
    });
    auto unknown =
        count_if(lottos.begin(), lottos.end(), [](auto e) { return e == 0; });
    return {
        mapping[matched + unknown],
        mapping[matched],
    };
}

int main(int argc, char const *argv[]) {
    auto a = solution({44, 1, 0, 0, 31, 25}, {31, 10, 48, 1, 6, 19});
    return 0;
}
