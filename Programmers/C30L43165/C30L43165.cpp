#include <string>
#include <vector>

using namespace std;

void rec(int &out, vector<int>::const_iterator be, vector<int>::const_iterator ed,
             int target, int current) {
    if (be == ed) {
        if(target == current){
            out += 1;
        }
        return;
    }
    rec(out, be + 1, ed, target, current + *be);
    rec(out, be + 1, ed, target, current - *be);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    rec(answer, numbers.begin(), numbers.end(), target, 0);
    return answer;
}