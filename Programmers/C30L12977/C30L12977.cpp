#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
using namespace std;

bool isprime(int v){
    if(v < 2){
        return false;
    }
    for(int i = 2; i <= v/2;i++){
        if(v % i == 0){
            return false;
        }
    }
    return true;
}

int solution(vector<int> nums) {
    int answer = 0;
    vector<bool> comb(nums.size() - 3, false);
    comb.insert(comb.end(), {true, true, true});
    do{
        auto it = comb.cbegin();
        auto v = accumulate(nums.cbegin(), nums.cend(), 0, [&it](auto acc, auto e){
            return acc + (*(it++)? e : 0);
        });
        answer += isprime(v) ? 1 : 0;
    }while(next_permutation(comb.begin(), comb.end()));

    return answer;
}