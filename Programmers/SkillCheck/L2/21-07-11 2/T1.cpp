#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<int> recur(vector<vector<int>> &arr, size_t r, size_t orix,
                  size_t oriy) {
    auto count = arr.size() / r;
    bool alleq = true;
    auto any = arr[oriy][orix];
    for (size_t y = oriy; y < oriy + r; y++) {
        for (size_t x = orix; x < orix + r; x++) {
            if (any != arr[y][x]) {
                alleq = false;
                break;
            }
        }
    }
    if (alleq) {
        if (any == 0) {
            return {1, 0};
        } else {
            return {0, 1};
        }
    } else {
        r = r / 2;
        auto lt = recur(arr, r, orix, oriy);
        auto rt = recur(arr, r, orix + r, oriy);
        auto rb = recur(arr, r, orix + r, oriy + r);
        auto lb = recur(arr, r, orix, oriy + r);
        return {
            lt[0] + rt[0] + rb[0] + lb[0],
            lt[1] + rt[1] + rb[1] + lb[1],
        };
    }
}
vector<int> solution(vector<vector<int>> arr) {
    return recur(arr, arr.size(), 0, 0);
}

int main() {
    // auto a = solution({{1, 1, 0, 0}, {1, 0, 0, 0}, {1, 0, 0, 1}, {1, 1, 1, 1}});
    
    auto a = solution({{1,1,1,1,1,1,1,1},{0,1,1,1,1,1,1,1},{0,0,0,0,1,1,1,1},{0,1,0,0,1,1,1,1},{0,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1},{0,0,0,0,1,0,0,1},{0,0,0,0,1,1,1,1}});
    cout << "{" << a[0] << ", " << a[1] << "}" << endl;
}