#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    for (size_t i = 1; i <= yellow; i++) {
        if (yellow % i == 0) {
            int h = i;
            int w = yellow / i;
            if (h > w) {
                break;
            }
            if ((w + 1) * 2 + (h + 1) * 2 == brown) {
                return {w, h};
            }
        }
    }

    return answer;
}