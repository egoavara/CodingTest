#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int dp_dfs(vector<string> &table, map<ptrdiff_t, int> &dpc,
           string::const_iterator be, string::const_iterator ed) {
    if (be == ed) {
        return 0;
    }
    // string t(be, ed);
    if (dpc.find(distance(be, ed)) != dpc.cend()) {
        return dpc[distance(be, ed)];
    }
    int result = -1;
    for (auto &w : table) {
        if (equal(w.begin(), w.end(), be)) {
            int tmp = dp_dfs(table, dpc, be + w.size(), ed);
            if (tmp != -1) {
                if (result == -1) {
                    result = tmp + 1;
                } else {
                    result = min(result, tmp + 1);
                }
            }
        }
    }
    dpc[distance(be, ed)] = result;
    return result;
}

int solution(vector<string> strs, string t) {
    map<ptrdiff_t, int> caches;
    sort(strs.begin(), strs.end(),
         [](auto a, auto b) { return a.size() > b.size(); });
    int answer = dp_dfs(strs, caches, t.cbegin(), t.cend());
    return answer;
}
int main(int argc, char const *argv[]) {
    // cout << solution({"ba", "an", "nan", "ban", "n"}, "banana") << endl;
    cout << solution({"app", "ap", "p", "l", "e", "ple", "pp"}, "apple")
         << endl;
    return 0;
}
