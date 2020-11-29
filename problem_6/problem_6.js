/**
 * Optimized using the formula.
 * sum_squares = (2n + 1)(n + 1)n / 6
 * sum = n(n + 1) / 2
 *
 * @param n
 * @returns {number}
 */
const difference = n => {
    return Math.pow((n * (n + 1) / 2), 2) - ((2 * n + 1) * (n + 1) * n / 6);
}

console.log(difference(100));

// Unoptimized
// More practice making an array using the spread operator and .keys().
const sum_difference = n => {
    const nums = [...Array(n + 1).keys()].slice(1);
    let sum_squares = nums.map(x => Math.pow(x, 2)).reduce((a, b) => a + b);
    let squared_sum = Math.pow(nums.reduce((a, b) => a + b), 2);
    return squared_sum - sum_squares;
}

console.log(sum_difference(100));