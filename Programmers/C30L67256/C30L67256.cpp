#include <string>
#include <vector>
#include <array>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    static array<int, 10> pmap{
        1 << 2 | 0, 
        0 << 2 | 3,
        1 << 2 | 3, 
        2 << 2 | 3,
        0 << 2 | 2, 
        1 << 2 | 2,
        2 << 2 | 2, 
        0 << 2 | 1,
        1 << 2 | 1, 
        2 << 2 | 1,
    };
    int lh = 0 << 2 | 0;
    int rh = 2 << 2 | 0;
    for(auto n : numbers){
        switch(n){
            case 1:
            case 4:
            case 7:
                answer += "L";
                lh = pmap[n];
                break;
            case 3:
            case 6:
            case 9:
                answer += "R";
                rh = pmap[n];
                break;
            case 2:
            case 5:
            case 8:
            case 0:
                auto dstx = pmap[n] >> 2;
                auto dsty = pmap[n] & 0x3;
                auto dl = abs((lh >> 2) - dstx) + abs((lh & 0x3) - dsty);
                auto dr = abs((rh >> 2) - dstx) + abs((rh & 0x3) - dsty);
                if(dl < dr){
                    answer += "L";
                    lh = pmap[n];
                }
                else if(dl > dr){
                    answer += "R";
                    rh = pmap[n];
                }
                else if(hand[0] == 'l'){
                    answer += "L";
                    lh = pmap[n];
                }else{
                    answer += "R";
                    rh = pmap[n];
                }
                break;
        }
        
    }
    return answer;
}