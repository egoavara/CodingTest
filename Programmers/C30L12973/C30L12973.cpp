#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int solution(string s) {
    vector<size_t> left;
    size_t right = 0;
    for (; right != s.length();right++) {
        if(left.empty()){
            left.push_back(right);
        }
        else if (s[*left.crbegin()] == s[right]) {
            left.pop_back();
        } else {
            left.push_back(right);
        }
    }
    return left.empty() ? 1 : 0;
}

int main() {
    auto a = solution("kcbaabcddefggfek");
    cout << "답 : " << a << endl;
}