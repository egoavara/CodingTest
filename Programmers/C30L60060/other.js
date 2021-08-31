class Node {
    constructor(value = '') {
        this.value = value
        this.count = 0
        this.end = false
        this.child = {}
    }
}
class Trie {
    constructor() {
        this.root = new Node
    }
    insert(words, node = this.root) {
        node.count +=1
        for (let word of words) {
            if (!node.child[word]) {
                node.child[word] = new Node(word)
            }
            node = node.child[word]
            node.count++
        }
        node.end = true
    }
    search(words, node = this.root) {
        let count = 0
        for (let word of words) {
            if (word == '?') {
                count++
            } else {
                if (node.child[word]) {
                    node = node.child[word]
                } else {
                    return 0
                }
            }
        }
        return node.count
    }
}
function solution(words, queries) {
    words = [... new Set(words)]
    var answer = [];
    let trieArray = Array.from({ length: 100000 }, () => false)
    for (let i = 0; i < words.length; i++) {
        if (!trieArray[words[i].length]) {
            trieArray[words[i].length] = [new Trie(), new Trie(), 0]
        }
        trieArray[words[i].length][0].insert(words[i])
        trieArray[words[i].length][1].insert(words[i].split('').reverse().join())
        trieArray[words[i].length][2]++
    }
    queries = queries.map(v => v[0] === '?' ? [v.split('').reverse().join(''), 1] : [v, 0])

    for (let i = 0; i < queries.length; i++) {
        console.log(JSON.stringify(trieArray[queries[i][0].length], undefined, '    ' ))
        if (trieArray[queries[i][0].length]) {
            if (queries[i][1] == 0) {
                answer.push(trieArray[queries[i][0].length][0].search(queries[i][0].split('').reverse().join()))
            } else {
                answer.push(trieArray[queries[i][0].length][1].search(queries[i][0]))
            }
        } else {
            answer.push(0)
        }
    }
    return answer;
}
console.log(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["?????"]))