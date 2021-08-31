#include <algorithm>
#include <cstdint>
#include <map>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

vector<int> solution(vector<string> info, vector<string> query) {
    // vector<int64_t> conds;
    map<int64_t, vector<pair<int, int>>> precalc;
    // vector<pair<int, int>> sorted_by_score;
    map<string, int64_t> flags{
        {"-", 0x000000},
        //
        {"java", 0x010000},
        {"cpp", 0x020000},
        {"python", 0x040000},
        //
        {"backend", 0x000100},
        {"frontend", 0x000200},
        //
        {"senior", 0x000010},
        {"junior", 0x000020},
        //
        {"chicken", 0x000001},
        {"pizza", 0x000002},
    };
    //
    for (int i = 0; i < info.size(); i++) {
        // smatch rematch;
        // regex_match(info[i], rematch, re_info);
        istringstream m(info[i]);
        string lang, side, cureer, favor, score;
        m >> lang;
        m >> side;
        m >> cureer;
        m >> favor;
        m >> score;
        auto flag_l = flags[lang];
        auto flag_s = flags[side];
        auto flag_c = flags[cureer];
        auto flag_f = flags[favor];
        auto data = make_pair(i, stoi(score));
        // conds.push_back(flag);
        precalc[flag_l | flag_s | flag_c | flag_f].push_back(data);
        //
        precalc[flag_s | flag_c | flag_f].push_back(data);
        precalc[flag_l | flag_c | flag_f].push_back(data);
        precalc[flag_l | flag_s | flag_f].push_back(data);
        precalc[flag_l | flag_s | flag_c].push_back(data);
        //
        precalc[flag_l | flag_s].push_back(data);
        precalc[flag_l | flag_c].push_back(data);
        precalc[flag_l | flag_f].push_back(data);
        precalc[flag_s | flag_c].push_back(data);
        precalc[flag_s | flag_f].push_back(data);
        precalc[flag_c | flag_f].push_back(data);
        //
        precalc[flag_l].push_back(data);
        precalc[flag_s].push_back(data);
        precalc[flag_c].push_back(data);
        precalc[flag_f].push_back(data);
        // 
        precalc[0].push_back(data);
        // sorted_by_score.push_back(data);
    }
    for (auto &l : precalc) {
        sort(l.second.begin(), l.second.end(),
             [&](auto &a, auto &b) { return a.second < b.second; });
    }
    // sort(sorted_by_score.begin(), sorted_by_score.end(),
    //      [](auto &a, auto &b) { return a.second < b.second; });
    vector<int> answer;
    for (string &q : query) {
        istringstream m(q);
        string lang, side, cureer, favor, score, discarding;
        m >> lang;
        m >> discarding;
        m >> side;
        m >> discarding;
        m >> cureer;
        m >> discarding;
        m >> favor;
        m >> score;
        int64_t filter =
            flags[lang] | flags[side] | flags[cureer] | flags[favor];
        int threshold = 0;
        if (score != "-") {
            threshold = stoi(score);
        }

        auto it = precalc[filter].begin(), ed = precalc[filter].end();
        for (; it != ed && it->second < threshold; it++) {
        }
        answer.push_back(distance(it, ed));
    }
    return answer;
}

int main(int argc, char const *argv[]) {
    auto a = solution(
        {"java backend junior pizza 150", "python frontend senior chicken 210",
         "python frontend senior chicken 150", "cpp backend senior pizza 260",
         "java backend junior chicken 80", "python backend senior chicken 50"},
        {"java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"});
    return 0;
}
