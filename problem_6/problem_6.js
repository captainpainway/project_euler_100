// Optimized
const difference = n => {
    return Math.pow((n * (n + 1) / 2), 2) - ((2 * n + 1) * (n + 1) * n / 6);
}

console.log(difference(100));