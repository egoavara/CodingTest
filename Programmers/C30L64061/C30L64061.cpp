#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    vector<vector<int>> boardT(board[0].size());
    vector<int> box;

    for_each(board.crbegin(), board.crend(), [&](auto &row) {
        for_each(row.cbegin(), row.cend(), [&, i = 0](auto elem) mutable {
            boardT[i++].push_back(elem);
        });
    });
    int answer = 0;
    for_each(moves.cbegin(), moves.cend(), [&](auto crane) {
        auto c = find_if(boardT[crane - 1].begin(), boardT[crane - 1].end(),
                         [](auto e) { return e == 0; });
        if (c != boardT[crane - 1].begin()) {
            if (!box.empty() && *box.rbegin() == *(c - 1)) {
                box.pop_back();
                answer += 2;
            } else {
                box.push_back(*(c - 1));
            }
            *(c - 1) = 0;
        }
    });
    return answer;
}

int main(int argc, char const *argv[]) {
    cout << solution({{0, 0, 0, 0, 0},
                      {0, 0, 1, 0, 3},
                      {0, 2, 5, 0, 1},
                      {4, 2, 4, 4, 2},
                      {3, 5, 1, 3, 1}},
                     {1, 5, 3, 5, 1, 2, 1, 4})
         << endl;
    return 0;
}
