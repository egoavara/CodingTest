#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;
#define POS_TO_MAT(w, x, y) (w * y + x)

bool is_linked(int n, int a, int b, const vector<char> &board2d) {
    int ax = a % n, ay = a / n;
    int bx = b % n, by = b / n;
    int minx = min(ax, bx), maxx = max(ax, bx);
    int miny = min(ay, by), maxy = max(ay, by);
    bool top = true, bot = true, lef = true, rig = true;
    for (int tempx = minx + 1; tempx < maxx; tempx++) {
        if (top && board2d[POS_TO_MAT(n, tempx, miny)] != '.') {
            top = false;
        }
        if (bot && board2d[POS_TO_MAT(n, tempx, maxy)] != '.') {
            bot = false;
        }
        if (!top && !bot){
            break;
        }
    }
    for (int tempy = miny + 1; tempy < maxy; tempy++) {
        if (rig && board2d[POS_TO_MAT(n, maxx, tempy)] != '.') {
            rig = false;
        }
        if (lef && board2d[POS_TO_MAT(n, minx, tempy)] != '.') {
            lef = false;
        }
        if (!lef && !rig){
            break;
        }
    }
    if (miny == maxy) {
        return top;
    }
    if (minx == maxx) {
        return lef;
    }
    if (ax < bx) {
        return (top && rig && (board2d[POS_TO_MAT(n, bx, ay)] == '.')) ||
               (lef && bot && (board2d[POS_TO_MAT(n, ax, by)] == '.'));
    } else {
        return (top && lef && (board2d[POS_TO_MAT(n, bx, ay)] == '.')) ||
               (rig && bot && (board2d[POS_TO_MAT(n, ax, by)] == '.'));
    }
}

// DFS
string solve(int m, int n, vector<char> &board2d,
             map<char, pair<int, int>> &char_at, string result) {
    bool is_allcomsume = true;
    for (auto elem = char_at.begin(); elem != char_at.end(); elem++) {
        int a = elem->second.first;
        int b = elem->second.second;
        if (board2d[a] == '.' && board2d[b] == '.') {
            continue;
        }
        is_allcomsume = false;
        if (is_linked(n, a, b, board2d)) {
            // sub
            board2d[a] = '.';
            board2d[b] = '.';
            auto subresult =
                solve(m, n, board2d, char_at, result + elem->first);
            if (subresult != "IMPOSSIBLE") {
                return subresult;
            }
            // restore
            board2d[a] = elem->first;
            board2d[b] = elem->first;
        }
    }
    return is_allcomsume ? result : "IMPOSSIBLE";
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(int m, int n, vector<string> board) {
    vector<char> board2d(m * n);

    map<char, pair<int, int>> char_at;
    for (int y = 0; y < m; y++) {
        for (int x = 0; x < n; x++) {
            char ch = board[y].at(x);
            if (isalpha(ch)) {
                if (char_at.find(ch) == char_at.end()) {
                    char_at[ch] = make_pair(POS_TO_MAT(n, x, y), -1);
                } else {
                    char_at[ch].second = POS_TO_MAT(n, x, y);
                }
            }
            board2d[POS_TO_MAT(n, x, y)] = ch;
        }
    }

    return solve(m, n, board2d, char_at, "");
}

int main(int argc, char const *argv[]) {
    string result;
    // result = solution(3, 3,
    //                   vector<string>{
    //                       "DBA",
    //                       "C*A",
    //                       "CDB",
    //                   });
    // cout << result << endl;
    // result = solution(2, 4,
    //                   vector<string>{
    //                       "NRYN",
    //                       "ARYA",
    //                   });
    // cout << result << endl;
    // result = solution(4, 4, vector<string>{".ZI.", "M.**", "MZU.", ".IU."});
    // cout << result << endl;
    // result = solution(2, 2, vector<string>{"AB", "BA"});
    // cout << result << endl;
    result = solution(3, 3, vector<string>{"CCB", "A.B", "AEE"});
    cout << result << endl;
    return 0;
}
