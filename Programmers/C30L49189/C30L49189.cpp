#include <algorithm>
#include <climits>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    int max_way_length = 0;
    vector<set<int>> edges(n);
    for_each(edge.cbegin(), edge.cend(), [&](auto a) {
        edges[a[0] - 1].insert(a[1] - 1);
        edges[a[1] - 1].insert(a[0] - 1);
    });

    vector<int> q_length{0};
    vector<int> q_route{0};
    vector<int> checked(n, -1);
    while (!q_route.empty()) {
        int loc = *q_route.cbegin();
        int len = *q_length.cbegin();
        q_route.erase(q_route.cbegin());
        q_length.erase(q_length.cbegin());
        if (checked[loc] == -1) {
            cout << loc << ", " << len << endl;
            checked[loc] = len;
            q_route.insert(q_route.cend(), edges[loc].cbegin(), edges[loc].cend());
            q_length.insert(q_length.cend(), edges[loc].size(), len + 1);
        }
    }

    return count(checked.cbegin(), checked.cend(),
                 *max_element(checked.cbegin(), checked.cend()));
}

int main(int argc, char const *argv[]) {
    cout << solution(6,
                     {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}})
         << endl;
    return 0;
}
