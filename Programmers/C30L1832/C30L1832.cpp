#include <iostream>
#include <vector>

using namespace std;

int MOD = 20170805;

void do_step(vector<vector<int>> &city_map, vector<vector<int>> &route_map,
             int ox, int oy, int dx, int dy) {
    if (oy + dy == 0 && ox + dx == 0) {
        route_map[oy + dy][ox + dx] = 1;
        return;
    }
    if (city_map[oy + dy][ox + dx] == 1) {
        route_map[oy + dy][ox + dx] = 0;
        return;
    }
    int left_x = ox + dx - 1, left_y = oy + dy;
    int top_x = ox + dx, top_y = oy + dy - 1;
    while (left_x >= 0 && city_map[left_y][left_x] == 2) {
        left_x--;
    }
    while (top_y >= 0 && city_map[top_y][top_x] == 2) {
        top_y--;
    }
    route_map[oy + dy][ox + dx] = ((left_x < 0 ? 0 : route_map[left_y][left_x]) +
                                  (top_y < 0 ? 0 : route_map[top_y][top_x])) % MOD;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
    vector<vector<int>> route_map(m, vector<int>(n));
    route_map[0][0] = 1;
    for (int w = n, h = m, ox = 0, oy = 0; w > 0 && h > 0;
         w--, h--, ox++, oy++) {
        for (int dx = 0; dx < w; dx++) {
            do_step(city_map, route_map, ox, oy, dx, 0);
        }
        for (int dy = 1; dy < h; dy++) {
            do_step(city_map, route_map, ox, oy, 0, dy);
        }
    }
    return route_map[m - 1][n - 1];
}

int main() {
    // cout << solution(3, 3, {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}) << endl;
    cout << solution(
                3, 6,
                {{0, 2, 0, 0, 0, 2}, {0, 0, 2, 0, 1, 0}, {1, 0, 0, 2, 2, 0}})
         << endl;
}