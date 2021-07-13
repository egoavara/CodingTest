#include <array>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solution(int n) {
    array<char, 3> mapping{'1', '2', '4'};
    string answer = "";
    for (; n > 0; n = (n-1) / 3) {
        answer = mapping[(n-1) % 3] + answer;
    }

    return answer;
}

int main(int argc, char const *argv[]) {
    cout << solution(1) << endl;
    cout << solution(2) << endl;
    cout << solution(3) << endl;
    cout << solution(4) << endl;
    cout << solution(5) << endl;
    cout << solution(6) << endl;
    cout << solution(7) << endl;
    cout << solution(8) << endl;
    cout << solution(9) << endl;
    cout << solution(10) << endl;
    cout << solution(11) << endl;
    cout << solution(12) << endl;
    cout << solution(13) << endl;
    cout << solution(14) << endl;
    return 0;
}
