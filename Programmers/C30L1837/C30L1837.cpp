#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <vector>

using namespace std;

int solve(map<int, set<int>> &route, int from, vector<int> &way) {
    //

}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, int m, vector<vector<int>> edge_list, int k,
             vector<int> gps_log) {
    map<int, set<int>> route;
    vector<vector<int>> table(k, vector<int>(n, numeric_limits<int>::max())); 
    for (int i = 0; i < n; i++) {
        route[i] = set<int>{i};
    }
    for (auto &&e : edge_list) {
        route[e[0] - 1].insert(e[1] - 1);
        route[e[1] - 1].insert(e[0] - 1);
    }
    return answer;
}
int main(int argc, char const *argv[]) {
    cout << solution(7, 10,
                     {{1, 2},
                      {1, 3},
                      {2, 3},
                      {2, 4},
                      {3, 4},
                      {3, 5},
                      {4, 6},
                      {5, 6},
                      {5, 7},
                      {6, 7}},
                     7, {1, 1, 1, 5, 1, 1, 7})
         << endl;
    return 0;
}
