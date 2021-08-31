#include <cmath>
#include <iostream>

using namespace std;

long long solution(int w, int h) {
    long long cnt = 0;
    double x = 0;
    double y = 0;
    double dydx = (double)h / (double)w;
    for (int i = 1; i <= w; i++) {
        double nx = i;
        double ny = y + dydx;
        cnt += (long long)(ceil(ny -0.00001) - floor(y));
        x = nx, y = ny;
    }
    return w * h - cnt;
}

int main(int argc, char const *argv[]) {
    cout << solution(8, 12) << endl;
    return 0;
}
