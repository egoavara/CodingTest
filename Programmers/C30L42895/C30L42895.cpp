#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

int nrepeat(const int n, const int rep) {
    int a = 0;
    for (int i = 0; i < rep; i++) {
        a = a * 10 + n;
    }
    return a;
}

const int MAX_DEPTH = 8;
int recur(const int n, const int target, const int depth,
          array<set<int>, MAX_DEPTH + 1> &mem) {
    if (depth > MAX_DEPTH) {
        return -1;
    }
    if (mem[depth].empty()) {
        mem[depth] = {nrepeat(n, depth)};
        for (size_t i = depth - 1; i >= 1; i--) {
            set<int>::const_iterator lbe = mem[i].cbegin(), led = mem[i].cend();
            set<int>::const_iterator rbe = mem[depth - i].cbegin(),
                                     red = mem[depth - i].cend();
            for (auto lv = lbe; lv != led; lv++) {
                for (auto rv = rbe; rv != red; rv++) {
                    mem[depth].insert(*lv + *rv);
                    mem[depth].insert(*lv - *rv);
                    mem[depth].insert(*lv * *rv);
                    if (*rv != 0) {
                        int adb = *lv / *rv;
                        mem[depth].insert(adb);
                    }
                }
            }
        }
        auto rf = find(mem[depth].cbegin(), mem[depth].cend(), target);
        if (rf != mem[depth].cend()) {
            return depth;
        }
        return recur(n, target, depth + 1, mem);
    }
}

int solution(int N, int number) {
    array<set<int>, MAX_DEPTH + 1> mem;
    mem[0] = {};
    return recur(N, number, 1, mem);
}

int main() {
    cout << solution(8, 53) << endl;
    return 0;
}