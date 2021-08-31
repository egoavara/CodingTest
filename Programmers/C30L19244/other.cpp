#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> r) {
    map<string, string> m;
    bool ch[100001];
    vector<string> ans, answer;
    int i;
    for (i = 0; i < r.size(); i++) {
        stringstream ss(r[i]);
        string s, s1, s2;
        ss >> s;
        ss >> s1;

        if (s == "Enter") {
            ss >> s2;
            m[s1] = s2;
            ans.push_back(s1);
            ch[i] = 1;
        } else if (s == "Leave") {
            ans.push_back(s1);
            ch[i] = 0;
        } else if (s == "Change") {
            ss >> s2;
            m[s1] = s2;
        }
    }
    for (i = 0; i < ans.size(); i++) {
        string st = m[ans[i]];
        if (ch[i]) {
            st += "님이 들어왔습니다.";
            answer.push_back(st);
        } else {
            st += "님이 나갔습니다.";
            answer.push_back(st);
        }
    }
    return answer;
}
int main(int argc, char const *argv[]) {
    auto a =
        solution({"Enter uid1234 Muzi ", "Enter uid4567 Prodo", "Leave uid1234",
                   "Change uid4567 Ryan", "Enter Uid1234 FALSE"});
    return 0;
}
