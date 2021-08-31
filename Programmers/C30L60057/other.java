package Programmers.C30L60057;

import java.util.*;

class Solution {
    public static void main(String[] args) {
        System.out.println(solution("a"));
    }
    public static int solution(String s) {
        int answers = s.length();
        int split = s.length() / 2;

        ArrayList<String> list = new ArrayList<String>();

        while(split != 0){
            int answer = s.length();
            int count = s.length() / split;
            for(int i=0; i<count; i++){
                list.add(s.substring(i*split, i*split+split));
            }

            String value = list.get(0);
            boolean check = false;
            int addCount = 1;
            int overlap = 1;
            for(int i=1; i<list.size(); i++){
                if(list.get(i).equals(value)){
                    addCount++;
                    if(addCount / (Math.pow(10, overlap)) == 1){
                        overlap++;
                        answer++;
                    }
                    if(!check){
                        answer =  answer - value.length() + 1;
                        check = true;
                    } else{
                        answer = answer - value.length();
                    }
                } else{
                    value = list.get(i);
                    check = false;
                }
            }

            split = split - 1;
            answers = answers > answer? answer: answers;
            list = new ArrayList<String>();
        }

        return answers;
    }
}