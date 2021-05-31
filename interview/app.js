// var intToRoman = function(int) {
//     const lookupMap = {
//         'M': 1000,
//         'CM': 900,
//         'D': 500,
//         'CD': 400,
//         'C': 100,
//         'XC': 90,
//         'L': 50,
//         'XL': 40,
//         'X': 10,
//         'IX': 9,
//         'V': 5,
//         'IV': 4,
//         'I': 1        
//     }
//     let roman_numeral = "";
//     while (int > 0) {
//         for (const numeral in lookupMap) {
//             while (int >= lookupMap[numeral]) {
//                 int -= lookupMap[numeral];
//                 roman_numeral += numeral;
//             }
//         }
//     }
//     return roman_numeral;
// };
// console.log(intToRoman(7))


// var oneAway = function(string1, string2) {
//     if ((string1.length - string2.length)**2 > 1){
//         return false
//     }
//     let count_difference = 0
//     for (let i = 0; i < Math.min(string1.length, string2.length); i++) {
//         if (string1[i] != string2[i]) {
//             count_difference += 1
//         }
//     }
//     return count_difference <= 1
// };

// console.log(oneAway("pales", "pale")) 

// const rotateMatrix = function(matrix) {
//     if (matrix.length === 0 || matrix.length === 1) return matrix;
//     transpose(matrix);
//     for (row of matrix) {
//         reverse(row, 0, row.length - 1)
//     }
//     return matrix
// }

// const transpose = function transpose(matrix) {
//     for (let i = 0; i < matrix.length; i++) {
//         for(let j = i; j < matrix[0].length; j++) {
//             const temp = matrix[i][j];
//             matrix[i][j] = matrix[j][i];
//             matrix[j][i] = temp;
//         }
//     }
//     return matrix; 
// }
// const reverse = function(row, start, end) {
//     while(start < end) {
//         const temp = row[start];
//         row[start] = row[end];
//         row[end] = temp
//         start += 1;
//         end -= 1;
//     }
//     return row;
// }
// matrix = [[1, 2, 4],[2, 0, 5], [2, 4, 3]]
// console.log(rotateMatrix(matrix))

// BFS Graphs
// const teams = "Madrid Athletico Barcelona Bayern Juventus PSG ManCity Inter".split(" ");
// const connections = [
//     ['Madrid', 'Athletico'],
//     ['Madrid', 'Barcelona'],
//     ['Madrid', 'Juventus'],
//     ['Barcelona', 'Bayern'],
//     ['Barcelona', 'PSG'],
//     ['ManCity', 'Bayern'],
//     ['Bayern', 'Inter'],
//     ['Inter', 'Juventus'],
// ]

// const adjacencyList = new Map();

// function addNode(team) {
//     adjacencyList.set(team, []);
// }

// function addEdge(origin, connection) {
//     adjacencyList.get(origin).push(connection);
//     adjacencyList.get(connection).push(origin);
// }

// teams.forEach(addNode);
// connections.forEach(connection => addEdge(...connection))

// function bfs(start) {
//     const queue = [start];
//     const visited = new Set();

//     while (queue.length > 0) {
//         const team = queue.shift();
//         const connections = adjacencyList.get(team);
//         for (const connection of connections) {

//             if (connection === 'PSG') {
//                 console.log("found PSG!")
//             };
 
//             if (!visited.has(connection)) {
//                 visited.add(connection);
//                 queue.push(connection);
//                 console.log(connection);
//             }
//         }
//     }
// }

// function dfs(start, visited = new Set()) {
//     console.log(start);
//     visited.add(start);
//     const connections = adjacencyList.get(start);

//     for (const connection of connections) {
//         if (connection === "PSG") {
//             console.log(`DFS found PSG in`)
//             return;
//         }
//         if (!visited.has(connection)) {
//             dfs(connection, visited);
//         }
//     }
// }
// //bfs("Madrid")
// dfs("Madrid")


// function binarySearch(array, target, start = 0, end = array.length-1) {
//     if (start > end) return `Target ${target} not in array`;
//     const mid = Math.floor((start+end)/2);
//     const mid_element = array[mid];

//     if (mid_element === target) {
//         return "Target " + target + " was found at position:" + mid
//     }
//     if (mid_element > target) {
//         return binarySearch(array, target, start, mid-1)
//     } else if (mid_element < target) {
//         return binarySearch(array, target, mid+1, end)
//     } 
// }
// console.log(binarySearch(array = [1,2,3,5,7,8,20, 23, 44, 99,220,400,5000,12315,90000], target = 5000))
function checkNextElements(haystack_slice, needle) {
    console.log(haystack_slice)
    if (haystack_slice === needle) {
        return true
    }
    return false  
}
 var strStr = function(haystack, needle) {
    const needleLen = needle.length;
     if (haystack.length === 0) {
         return 0
     }
     let return_value = -1
     for (let i = 0; i < haystack.length; i++) {
         if (haystack[i] === needle[0]){
            if (checkNextElements(haystack.slice(i, i + needleLen), needle)) {
                return i
            }
         }
     }
     return -1 
};



console.log(strStr(haystack = "hello", needle = "ll"))