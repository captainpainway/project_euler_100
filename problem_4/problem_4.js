const find_palindrome = n => {
    return n === +n.toString().split("").reverse().join("");
}

// Clever and functional, but hard to reason with.
const find_largest = () => {
    const arr = Array(900).fill(0).map((_, i) => 999 - i);
    return arr.reduce((acc, a) => {
        acc.push(arr.filter(b => find_palindrome(a * b) ? b : null).map(n => n * a));
        return acc;
    }, []).flat().sort((a, b) => b - a)[0];
}

const find_largest_loop = () => {
    let max = 999,
        largest = 0;
    while (max > 100) {
        let max2 = max;
        if (max * max2 < largest) {
            break;
        }
        while (max2 > 100) {
            if (find_palindrome(max * max2) && (max * max2 > largest)) {
                largest = max * max2;
            }
            max2--;
        }
        max--;
    }
    return largest;
}

console.log(find_largest_loop(), "loop");
console.log(find_largest(), "reduce");
