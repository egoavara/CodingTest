function solution(b, m) {
    var answer = []
    var board = []
    var result = 0;
    for (var i = 0; i < b.length; i++) {
        var line = []
        for (var j = 0; j < b[i].length; j++) {
            if (b[j][i] !== 0) { line.push(b[j][i]) }
        }
        board.push(line)
    }
    console.log(board)
    for (var x = 0; x < m.length; x++) {
        m[x] = m[x] - 1
    }

    for (var y = 0; y < m.length; y++) {
        answer.push(board[m[y]][0])
        board[m[y]].splice(0, 1)
    }
    var af = answer.filter((b) => { return undefined !== b })
    af = [1,1,2,2,3]
    console.log(answer)
    console.log(af)
    for (var a = 0; a < af.length; a++) {
        console.log(`Slice af[${a}:]${af.slice(a)}`)
        if (af[a] === af[a + 1]) {
            af.splice(a, 2)
            a = 0
            result += 2
            console.log(af, a)
        }
    }
    return result
}

// console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 1, 4]))
// console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 1, 4]))
