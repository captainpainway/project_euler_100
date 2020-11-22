const fib = (n) => {
    let arr = [1, 2];
    let [a, b] = arr;
    while (b < n) {
        let c = a + b;
        a = b;
        b = c;
        arr.push(c)
    }
    arr.pop();
    return arr.filter(x => x % 2 === 0).reduce((a, b) => a + b);
}

console.log(fib(4000000));