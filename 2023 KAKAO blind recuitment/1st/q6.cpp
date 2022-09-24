#include <string>
#include <vector>

using namespace std;

string dfs(int n, int m, int r, int c, int k, int cx, int cy, string way) {
    int dx = abs(cx - r);
    int dy = abs(cy - c);
    if ((dx + dy) > (k - way.length())) {
        return "impossible";
    }
    if (cx <= 0 || cx > n || cy <= 0 || cy > m) {
        return "impossible";
    }
    if (way.length() == k) {
        if (cx == r && cy == c) {
            return way;
        }
        return "impossible";
    }
    string wh;
    //
    wh = dfs(n, m, r, c, k, cx + 1, cy, way + "d");
    if (wh != "impossible") {
        return wh;
    }
    //
    wh = dfs(n, m, r, c, k, cx, cy - 1, way + "l");
    if (wh != "impossible") {
        return wh;
    }
    //
    wh = dfs(n, m, r, c, k, cx, cy + 1, way + "r");
    if (wh != "impossible") {
        return wh;
    }
    //
    wh = dfs(n, m, r, c, k, cx - 1, cy, way + "u");
    if (wh != "impossible") {
        return wh;
    }
    return "impossible";
}
string solution(int n, int m, int x, int y, int r, int c, int k) {
    int dx = abs(x - r);
    int dy = abs(y - c);
    int da = dx + dy;
    if((k - da) % 2 == 1){
        return "impossible";
    }
    return dfs(n, m, r, c, k, x, y, "");
}