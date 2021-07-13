#include <iostream>
#include <string>
#include <stack>
using namespace std;

int solution(string s) {
    stack<size_t> left;
    stack<size_t> right;
    left.push(0);
    for (size_t i = s.length()-1; i >0; i--)
    {
        right.push(i);
    }
    
    for (;!right.empty();) {
        if (s[left.top()] == s[right.top()]) {
            left.pop();
            right.pop();
            if(left.empty() && !right.empty()){
                left.push(right.top());
                right.pop();
            }
        } else {
            left.push(right.top());
            right.pop();
        }
    }
    return left.empty() && right.empty() ? 1 : 0;
}

int main() {
    auto a = solution("kcbaabcddefggfek");
    cout << "답 : " << a << endl;
}