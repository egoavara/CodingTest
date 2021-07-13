#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int N, int number);
int dcalc(const int N, const int number, const int Nn, const int C);

int main() {
    cout << solution(2, 11) << endl;
    return 0;
}

int solution(int N, int number) {
    int answer = dcalc(N, number, N, 1);
    return answer > 8 ? -1 : answer;
}

array<int, 32001> mem;

int dcalc(const int N, const int number, const int Nn, const int C) {
    if (C > 8 || number < 0) {
        return 8;
    }
    if (number == 0) {
        return C;
    }
    if ( number < 32001 && mem[number] != 0) {
        return mem[number];
    }
    int answer = min({
        dcalc(N, number, Nn * 10 + N, C + 1),
        dcalc(N, number - Nn, N, C + 1),
        dcalc(N, number + Nn, N, C + 1),
        dcalc(N, number / Nn, N, C + 1),
        dcalc(N, number * Nn, N, C + 1),
    });
    if ( number < 32001) {
        mem[number] = answer;
    }
    return answer;
}
