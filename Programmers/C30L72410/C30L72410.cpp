#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    int prev = 0;
    //
    transform(new_id.begin(), new_id.end(), new_id.begin(),
              [](auto c) { return tolower(c); });
    //
    new_id.erase(remove_if(new_id.begin(), new_id.end(), [](auto c) {
        return !(islower(c) || isdigit(c) || c == '-' || c == '_' || c == '.');
    }), new_id.end());
    //
    new_id.erase(remove_if(new_id.begin(), new_id.end(), [&prev](auto c) {
        auto a = prev == '.' && c == '.';
        prev = c;
        return a;
    }), new_id.end());
    //
    if (*new_id.begin() == '.') {
        new_id.erase(new_id.begin());
    }
    if (*(new_id.end() - 1) == '.') {
        new_id.erase(new_id.end() - 1);
    }
    //
    if (new_id.empty()) {
        new_id.push_back('a');
    }
    //
    if (new_id.size() >= 16) {
        new_id.erase(new_id.begin() + 15, new_id.end());
    }
    if (*(new_id.end() - 1) == '.') {
        new_id.erase(new_id.end() - 1);
    }
    //
    if (new_id.size() <= 2) {
        generate_n(back_inserter(new_id), 3 - new_id.size(),
                   [lc = *new_id.rbegin()]() { return lc; });
    }

    return new_id;
}

int main() {
    // cout << solution("....!@BaT#*..y.abcdefghijklm") << endl;
    // cout << solution("ab") << endl;
    cout << solution("b") << endl;
}