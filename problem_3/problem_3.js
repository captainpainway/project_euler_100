// From the project Euler overview - much faster
const faster_prime_factor = n => {
    let factor = 2,
        last_factor = 1;
    while (n > 1) {
        if (n % factor === 0) {
            last_factor = factor;
            n = n / factor;
        } else {
            factor++;
        }
    }
    return last_factor;
}

console.log(faster_prime_factor(13195));
console.log(faster_prime_factor(600851475143));

const largest_prime_factor = n => {
    return sieve_of_eratosthenes(Math.ceil(Math.sqrt(n) / 2))
        .reverse()
        .find(p => n % p === 0);
}

// Using an object is much faster
// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
// In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
const sieve_of_eratosthenes = sq => {
    let arr = [...Array(sq).keys()].slice(2);
    let idx = 0;
    let next_prime = 0;
    let deletes = {};
    while (next_prime < Math.ceil(arr.length / 4)) {
        next_prime = arr[idx];
        [...Array(sq).keys()]
            .slice(idx + 1)
            .filter(x => x % next_prime === 0 && x > next_prime)
            .forEach(v => deletes[v] = v);
        arr = arr
            .filter(n => !deletes[n]);
        idx++;
    }
    return arr;
}

// console.log(largest_prime_factor(13195));
// console.log(largest_prime_factor(600851475143));

// This takes forever
// It was finding all the primes up to the given number, then removing non-primes from the array.
const old_sieve = sq => {
    let arr = [...Array(sq).keys()].slice(2);
    let idx = 0;
    let next_prime = 0;
    while (next_prime < Math.ceil(arr.length / 4)) {
        next_prime = arr[idx];
        let deletes = [...Array(sq).keys()].slice(idx + 1).filter(x => x % next_prime === 0);
        arr = arr
            .filter(n => !deletes.includes(n));
        idx++;
    }
    return arr.filter(x => x);
}
