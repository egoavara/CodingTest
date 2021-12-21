#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
#define MAT2D_POS(w, x, y) (w * y + x)
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
string solution(int m, int n, vector<string> board) {
    vector<char> board2d(m * n);
    for_each(board.cbegin(), board.cend(), [&, i = 0](string a) mutable {
        for_each(a.cbegin(), a.cend(), [&](char c) { board2d[i++] = c; });
    });

    string answer = "";
    return answer;
}