const sieve_of_eratosthenes = n => {
    let arr = [...Array(n).keys()].slice(2);
    let next_prime = 0;
    let idx = 0
    while (next_prime < Math.ceil(arr.length / 2)) {
        next_prime = arr[idx];
        let deletes = arr
            .slice(idx + 1)
            .filter(x => x % next_prime === 0);
        arr = arr
            .filter(n=> !deletes.includes(n))
        idx++;
    }
    return arr.filter(x => x);
}

const smallest_multiple = n => {
    let primes = sieve_of_eratosthenes(n);
    let powers = primes.map(x => Math.floor(Math.log(n)/Math.log(x)));
    return primes
        .map((y, i) => y ** powers[i])
        .reduce((a, b) => a * b);
}

console.log(smallest_multiple(20));
