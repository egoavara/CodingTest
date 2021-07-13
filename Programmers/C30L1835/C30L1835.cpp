#include <array>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
void recur(int &out, array<char, 8> l, vector<string>::const_iterator be,
           vector<string>::const_iterator ed) {
    if (be == ed) {
        out++;
        return;
    }
    char a = (*be)[0], b = (*be)[2], op = (*be)[3];
    int param = (*be)[4] - '0';
    int al = distance(l.cbegin(), find(l.cbegin(), l.cend(), a));
    int bl = distance(l.cbegin(), find(l.cbegin(), l.cend(), b));
    switch (op) {
        case '=':
            if (al == 8 && bl == 8) {
                for (size_t i = 0; i < 8 - param - 1; i++) {
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
                // TODO
            } else {
                // TODO
            }
            break;
        case '<':
            // TODO
            break;
        case '>':
            if (al == 8 && bl == 8) {
                for (size_t i = 0; i < 8 - param - 1; i++) {
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
                // TODO
            } else {
                // TODO
            }
            break;
    }
}
int solution(int n, vector<string> data) {
    int answer = 0;
    recur(answer, {'-', '-', '-', '-', '-', '-', '-', '-'}, data.cbegin(),
          data.cend());
    return answer;
}
int main(int argc, char const *argv[]) {
    cout << solution(2, {"N~F=0", "R~T>2"}) << endl;
    return 0;
}
