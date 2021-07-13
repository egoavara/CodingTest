function solution(new_id) {
    var answer = '';
    answer = new_id.toLowerCase();
    answer = answer.replace(/[^\w-._]+/gi,'');
    answer = answer.replace(/\.\.+/g,'.');
    answer = answer.replace(/\.$/g,'');
    answer = answer.replace(/^\./g,'');
    if(answer == '') answer = new_id.replace(/./g,'a');
    if(answer.length >= 16){
        var newAnswer = answer.substr(0,15);
        answer = newAnswer.replace(/\.$/g,''); 
    }
    if(answer.length <= 2){
        var newAnswer = answer.substr(answer.length-1,1);
        for(var i = answer.length; i < 3; i++){
            answer = answer + newAnswer;
        }
    }

    return answer;
}

console.log(solution(""))

const a = ''
let b = 'a'
b= b.replace(/a+/g, '')
console.log(a, a == '')
console.log(b, b == '')