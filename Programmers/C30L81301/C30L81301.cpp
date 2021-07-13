#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    for(size_t i = 0; i < s.size();){
        if(isdigit(s[i])){
            answer = answer * 10 + (s[i] - '0');
            i++;
        }else{
            switch(s[i] ^ s[i+1]){
            case 'z' ^ 'e':     
                answer = answer * 10 + 0;
                i += 4;
                break;
            case 'o' ^ 'n':     
                answer = answer * 10 + 1;
                i += 3;
                break;
            case 't' ^ 'w':     
                answer = answer * 10 + 2;
                i += 3;
                break;
            case 't' ^ 'h':     
                answer = answer * 10 + 3;
                i += 5;
                break;
            case 'f' ^ 'o':     
                answer = answer * 10 + 4;
                i += 4;
                break;
            case 'f' ^ 'i':     
                answer = answer * 10 + 5;
                i += 4;
                break;
            case 's' ^ 'i':     
                answer = answer * 10 + 6;
                i += 3;
                break;
            case 's' ^ 'e':     
                answer = answer * 10 + 7;
                i += 5;
                break;
            case 'e' ^ 'i':     
                answer = answer * 10 + 8;
                i += 5;
                break;
            case 'n' ^ 'i':     
                answer = answer * 10 + 9;
                i += 4;
                break;
            }
        }
    }
    return answer;
}