#include <algorithm>
#include <cctype>
#include <map>
#include <string>
#include <vector>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(int m, int n, vector<string> board) {
    map<char, vector<pair<int, int>>> locs;
    for (size_t row = 0; row < m; row++) {
        for (size_t col = 0; col < n; col++) {
            if (isalpha(board[row][col])) {
                locs[board[row][col]].push_back(make_pair(row, col));
            }
        }
    }

    string answer = "";
    return answer;
}