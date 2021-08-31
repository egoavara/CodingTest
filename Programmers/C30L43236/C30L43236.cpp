#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    sort(rocks.begin(), rocks.end());
    rocks.push_back(distance);
    for (size_t i = rocks.size() - 1; i >= 1; i--) {
        rocks[i] -= rocks[i - 1];
    }

    int mn = 1, mx = distance;
    while (mn < mx) {
        int md = (mx + mn) / 2;
        vector<int> copyed(rocks.cbegin(), rocks.cend());
        int delcnt = 0;
        for (; delcnt < n; delcnt++) {
            auto target = find_if(copyed.begin(), copyed.end(),
                                  [=](auto e) { return e != -1 && e <= md; });
            if (target == copyed.end()) {
                break;
            }
            if (target + 1 != copyed.end()) {
                *(target + 1) += *target;
            } else {
                *(target - 1) += *target;
            }
            *target = -1;
        }

        if (delcnt != n) {
            mn = md + 1;
        } else {
            if (*min_element(copyed.begin(), copyed.end(), [](auto a, auto b) {
                    return (a != -1 ? a : b - 1) < (b != -1 ? b : a + 1);
                }) > md) {
                    mn = md + 1;
            }else{
                mx = md;
            }
        }
    }

    return mn;
}

int main(int argc, char const *argv[]) {
    // cout << solution(25, {2, 14, 11, 21, 17}, 2) << endl;
    // cout << solution(18, {2, 8, 9, 10, 11, 12, 13}, 6) << endl;
    // cout << solution(34, {5, 19, 28}, 2) << endl;
    cout << solution(1234, {1, 2, 3}, 3) << endl;
    return 0;
}
