const util = require('util')


function solution(numbers) {
    var answer = [];

    for (let i = 0; i < numbers.length; i++) {
        let str = '0' + numbers[i].toString(2);

        let zeroIdx = str.lastIndexOf('0');
        console.log(str.length)
        if (zeroIdx === str.length - 1) {
            // 마지막 인덱스인 경우
            answer.push(Number(BigInt(numbers[i]) ^ BigInt(1)));
        } else {
            // 첫 번째 인덱스인 경우
            let temp = '11' + '0'.repeat(str.length - 1 - zeroIdx - 1);
            answer.push(Number(BigInt(parseInt(str, 2)) ^ BigInt(parseInt(temp, 2))));
        }
    }

    return answer;
}

console.dir(solution([1000000000000000, 100000000000001]), { 'maxArrayLength': 
null })
console.log(1000000000000000 ^ 1)
