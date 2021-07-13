#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    auto l = s.begin();
    auto r = s.begin();
    do {
        l = r;
        for (; l != s.end() && *l == ' '; l++) {
        }
        r = l + 1;
        for (; r != s.end() && *r != ' '; r++) {
        }
        *l = toupper(*l);
        for (auto c = l + 1; c != r; c++) {
            *c = tolower(*c);
        }

    } while (l != s.end() && r != s.end());
    return s;
}
int main() {
    auto a = solution("3people unFollowed me");
    cout << "답 : " << a << endl;
}