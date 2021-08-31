#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

array<int, 9> facto_results = {1, 1, 2, 6, 24, 120, 720, 5040, 40320};

void recur(int &out, array<char, 8> l, vector<string>::const_iterator be,
           vector<string>::const_iterator ed) {
    if (be == ed) {
        cout << l[0] << l[1] << l[2] << l[3] << l[4] << l[5] << l[6] << l[7]
             << " : "
             << facto_results[count_if(l.cbegin(), l.cend(),
                                       [](auto e) { return e == '-'; })]
             << endl;
        out += facto_results[count_if(l.cbegin(), l.cend(),
                                      [](auto e) { return e == '-'; })];
        return;
    }
    char a = (*be)[0], b = (*be)[2], op = (*be)[3];
    int param = (*be)[4] - '0';
    int al = distance(l.cbegin(), find(l.cbegin(), l.cend(), a));
    int bl = distance(l.cbegin(), find(l.cbegin(), l.cend(), b));
    switch (op) {
        case '=':
            if (al == 8 && bl == 8) {
                for (size_t i = 0; i < 8; i++) {
                    if (l[i] == '-' && l[i + param + 1] == '-') {
                        array<char, 8> ab = l;
                        ab[i] = a;
                        ab[i + param + 1] = b;
                        recur(out, ab, be + 1, ed);
                        array<char, 8> ba = l;
                        ba[i] = b;
                        ba[i + param + 1] = a;
                        recur(out, ba, be + 1, ed);
                    }
                }

            } else if (al != 8 && bl != 8) {
                if (abs(al - bl) - 1 != param) {
                    return;
                }
                recur(out, l, be + 1, ed);
            } else {
                int existl = a == 8 ? bl : al;
                int notexistc = a == 8 ? a : b;
                if ((existl - param - 1) >= 0 && l[existl - param - 1] == '-') {
                    array<char, 8> ab = l;
                    ab[existl - param - 1] = notexistc;
                    recur(out, ab, be + 1, ed);
                }
                if ((existl + param + 1) < 8 && l[existl + param + 1] == '-') {
                    array<char, 8> ab = l;
                    ab[existl + param + 1] = notexistc;
                    recur(out, ab, be + 1, ed);
                }
            }
            break;
        case '<':
            if (al == 8 && bl == 8) {
                for (size_t i = 0; i < 8; i++) {
                    if (l[i] == '-') {
                        for (size_t j = 0; j < param; j++) {
                            if ((i + j + 1) < 8 && l[i + j + 1] == '-') {
                                array<char, 8> ab = l;
                                ab[i] = a;
                                ab[i + j + 1] = b;
                                recur(out, ab, be + 1, ed);
                                array<char, 8> ba = l;
                                ba[i] = b;
                                ba[i + j + 1] = a;
                                recur(out, ba, be + 1, ed);
                            }
                        }
                    }
                }

            } else if (al != 8 && bl != 8) {
                if ((abs(bl - al) - 1) >= param) {
                    return;
                }
                recur(out, l, be + 1, ed);
            } else {
                int existl = a == 8 ? bl : al;
                int notexistc = a == 8 ? a : b;
                for (int i = 0; i < param; i++) {
                    if ((existl - i - 1) >= 0 && l[existl - i - 1] == '-') {
                        array<char, 8> ab = l;
                        ab[existl - i - 1] = notexistc;
                        recur(out, ab, be + 1, ed);
                    }
                    if ((existl + i + 1) < 8 && l[existl + i + 1] == '-') {
                        array<char, 8> ab = l;
                        ab[existl + i + 1] = notexistc;
                        recur(out, ab, be + 1, ed);
                    }
                }
            }

            break;
        case '>':
            if (al == 8 && bl == 8) {
                for (size_t i = 0; i < 8; i++) {
                    if (l[i] == '-') {
                        for (size_t j = param + 1; j <= 6; j++) {
                            if ((i + j + 1) < 8 && l[i + j + 1] == '-') {
                                array<char, 8> ab = l;
                                ab[i] = a;
                                ab[i + j + 1] = b;
                                recur(out, ab, be + 1, ed);
                                array<char, 8> ba = l;
                                ba[i] = b;
                                ba[i + j + 1] = a;
                                recur(out, ba, be + 1, ed);
                            }
                        }
                    }
                }

            } else if (al != 8 && bl != 8) {
                if ((abs(bl - al) - 1) <= param) {
                    return;
                }
                recur(out, l, be + 1, ed);
            } else {
                int existl = a == 8 ? bl : al;
                int notexistc = a == 8 ? a : b;
                for (int i = param + 1; i <= 6; i++) {
                    if ((existl - i - 1) >= 0 && l[existl - i - 1] == '-') {
                        array<char, 8> ab = l;
                        ab[existl - i - 1] = notexistc;
                        recur(out, ab, be + 1, ed);
                    }
                    if ((existl + i + 1) < 8 && l[existl + i + 1] == '-') {
                        array<char, 8> ab = l;
                        ab[existl + i + 1] = notexistc;
                        recur(out, ab, be + 1, ed);
                    }
                }
            }
            break;
    }
}

int permut(vector<string>::const_iterator be,
           vector<string>::const_iterator ed) {
    array<char, 8> l{'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    int out = 0;
    do {
        auto c = be;
        for (; c != ed; c++) {
            char a = (*c)[0], b = (*c)[2], op = (*c)[3];
            int param = (*c)[4] - '0';
            int dist = abs(distance(find(l.cbegin(), l.cend(), a),
                                find(l.cbegin(), l.cend(), b))) - 1;
            if (op == '=' && dist != param) {
                break;
            } else if (op == '<' && dist >= param) {
                break;
            } else if (op == '>' && dist <= param) {
                break;
            }
        }
        if (c == ed) {
            out++;
        }

    } while (next_permutation(l.begin(), l.end()));
    return out;
}
int solution(int n, vector<string> data) {
    // int answer = 0;
    // recur(answer, {'-', '-', '-', '-', '-', '-', '-', '-'}, data.cbegin(),
    //       data.cbegin() + n);
    // return answer;
    return permut(data.cbegin(), data.cbegin() + n);
}

int main(int argc, char const *argv[]) {
    cout << solution(2, {"N~F=0", "R~T>2"}) << endl;
    // cout << solution(2, {"N~F=0", "N~T>1", "N~T>1", "N~T>1"}) << endl;
    // cout << solution(2, {"A~C=0", "F~J=0", "M~N=0", "R~T=0"}) << endl;
    // cout << solution(2, {"M~C<2", "C~M>1"}) << endl;
    return 0;
}
