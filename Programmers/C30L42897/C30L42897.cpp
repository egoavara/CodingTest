#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> money) {
    //
    vector<int> caching0(money.size()+1, 0);
    caching0[money.size() - 2] = money[money.size() - 2];
    // caching0[money.size() - 1] = 0;
    for (int cur = money.size() - 3; cur >= 0; cur--) {
        caching0[cur] = money[cur] + max(caching0[cur + 2], caching0[cur + 3]);
    }
    //
    vector<int> caching1(money.size() + 2, 0);
    caching1[money.size() - 1] = money[money.size() - 1];
    // caching1[money.size()] = 0;
    for (int cur = money.size() - 2; cur >= 1; cur--) {
        caching1[cur] = money[cur] + max(caching1[cur + 2], caching1[cur + 3]);
    }

    int a = max({caching0[0], caching0[1], caching1[1], caching1[2]});
    return a;
}

// int main() { cout << solution({1, 2, 3, 1}) << endl; }
int main() {
    // cout << solution({123, 230, 312, 125, 123, 127, 129}) << endl;
    // cout << solution({1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000}) << endl;
    // cout << solution({1,2,3,4,5,6,7,8,9,10}) << endl;
    // cout << solution({11,0,2,5,100,100,85,1}) << endl;
    // cout << solution({91,90,5,7,5,7}) << endl;
    cout << solution({90, 0, 0, 95, 1, 1}) << endl;
    // cout << solution({90, 0, 0, 0, 95, 1, 1}) << endl;
    // cout << solution({0,0,0,95,1,90}) << endl;
}
