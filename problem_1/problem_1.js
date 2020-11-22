const multiples = (n) => {
    return [...Array(n).keys()]
        .filter((x) => x % 3 === 0 || x % 5 === 0)
        .reduce((a, b) => a + b, 0);
}

console.log(multiples(1000));