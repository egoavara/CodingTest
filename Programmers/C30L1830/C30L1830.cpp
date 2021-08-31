#include <algorithm>
#include <iostream>
#include <numeric>
#include <regex>
#include <set>
#include <string>
#include <vector>

using namespace std;

std::regex mix_style("^([a-z])[A-Z](?!\\1)([a-z])[A-Z](\\2[A-Z])*\\1");
std::regex repeat_style("^[A-Z]([a-z])[A-Z](\\1[A-Z])*");
std::regex wrap_style("^([a-z])[A-Z]+\\1");
std::regex just_style("^[A-Z]+");
std::regex left_style("^[A-Z]+(?=[A-Z])");

bool is_used_char(smatch target, set<char> &used) {
    if (!target.ready()) {
        return true;
    }

    if (target.size() > 1 && target[1].length() == 1 &&
        islower(target[1].str()[0]) &&
        used.end() != used.find(target[1].str()[0])) {
        return true;
    }
    if (target.size() > 2 && target[2].length() == 1 &&
        islower(target[2].str()[0]) &&
        used.end() != used.find(target[2].str()[0])) {
        return true;
    }
    return false;
}

pair<bool, string> parse(string sentence, set<char> &used) {
    if (sentence.length() == 0) {
        return make_pair(true, string());
    }
    string suffix = "";
    vector<smatch> restore(5);
    regex_search(sentence, restore[0], mix_style);
    regex_search(sentence, restore[1], wrap_style);
    regex_search(sentence, restore[2], repeat_style);
    regex_search(sentence, restore[3], left_style);
    regex_search(sentence, restore[4], just_style);
    for (auto &&i : restore) {
        if (i.ready() && i.size() != 0 && !is_used_char(i, used)) {
            vector<char> current_used;
            if (i.size() > 1 && i[1].length() == 1 && islower(i[1].str()[0])) {
                current_used.push_back(i[1].str()[0]);
            }
            if (i.size() > 2 && i[2].length() == 1 && islower(i[2].str()[0])) {
                current_used.push_back(i[2].str()[0]);
            }
            //
            for (auto &&ch : current_used) {
                used.insert(ch);
            }
            //
            auto suffix_res = parse(i.suffix().str(), used);
            if (suffix_res.first) {
                string matched = i.str();
                string captured;
                std::copy_if(matched.cbegin(), matched.cend(),
                             back_inserter(captured),
                             [](auto c) { return isupper(c); });
                if (suffix_res.second.length() > 0) {
                    captured += " " + suffix_res.second;
                }
                return make_pair(true, captured);
            }
            //
            for (auto &&ch : current_used) {
                used.erase(ch);
            }
        }
    }
    return make_pair(false, string());
}

string solution(string sentence) {
    set<char> used_chars;
    auto result = parse(sentence, used_chars);
    if (result.first) {
        return result.second;
    } else {
        return "invalid";
    }
}

int main(int argc, char const *argv[]) {
    // cout << solution("IAMLOONGHaEaLaLaObWORLDbCCC") << endl;
    // cout << solution("bWORLDbCCC") << endl;
    // cout << solution("SpIpGpOpNpGJqOqA") << endl;
    // cout << solution("AxAxAxAoBoBoB") << endl;
    // cout << solution("AxAxAxAoAo") << endl;
    // cout << "'" << solution("AxAAcA") << "'" << endl;
    // cout << "'" << solution("xABCx") << "'" << endl;
    // cout << "'" << solution("AxBxCxD") << "'" << endl;
    // cout << "'" << solution("AbAaAbAaCa") << "'" << endl;
    // cout << "'" << solution("aHbEbLbLbOacWdOdRdLdDc") << "'" << endl;
    // cout << "'" << solution("abHbEbLbLbObacWdOdRdLdDc") << "'" << endl;
    // cout << "'" << solution("AAAAAAA") << "'" << endl;
    // cout << "'" << solution("cAAAAAAAc") << "'" << endl;
    // cout << "'" << solution("cccccccccccc") << "'" << endl;
    // cout << "'" << solution("HaEaLaLObWORLDb") << "'" << endl;
    // cout << "'" << solution("abHELLObaWORLD") << "'" << endl;
    // cout << "'" << solution("abHba") << "'" << endl;
    // cout << "'" << solution("aHELLOWORLDa ") << "'" << endl;
    // cout << "'" << solution("HaEaLaLaOWbObRbLbD") << "'" << endl;
    // cout << "'" << solution("aAaCbBb") << "'" << endl;
    // cout << "'" <<
    // solution("AAAaBaAbBBBBbCcBdBdBdBcCeBfBeGgGGjGjGRvRvRvRvRvR")
    //      << "'" << endl;
    // cout << "'" << solution("AcAcABaBaB") << "'" << endl;
    // cout << "'" << solution("AcAcAcAcAcAcA") << "'" << endl;
    // cout << "'" << solution("cAAAAAAAccAAAAAAAc") << "'" << endl;
    // cout << "'" << solution("dAcAcAcAcAcAcAd") << "'" << endl;
    // cout << "'" << solution("dcAcAcAcAcAcAcAcd") << "'" << endl;
    // cout << "'" << solution("abHbEbLbLbOba") << "'" << endl;
    // cout << "'" << solution("aaHaEaLaLaOaa") << "'" << endl;
    return 0;
}
