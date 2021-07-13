#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    auto isign = signs.begin();
    
    return accumulate(absolutes.cbegin(), absolutes.cend(), 0, [&isign](auto acc, auto e){
        return acc + (*(isign++) ? e : -e);
    });
}