// compile with rustc problem_5.rs
// run as ./problem_5

/**
    Optimized to push the prime ^ pow directly to the powers vector,
    instead of pushing the power and doing that calculation later.
    Saves a step before the .fold().
**/
fn main() {
    let n = 20;
    let primes = prime_sieve(n);
    let mut powers = Vec::new();
    for x in primes {
        let mut i = 1;
        while x.pow(i) < n {
            i += 1;
        }
        powers.push(x.pow(i - 1));
    }
    let num = powers.into_iter().fold(1, |a, b| a * b);
    println!("{:?}", num);
}

/**
    Doing this sieve slightly differently.
    See problem 7.
    Dividing each number in the range by previous primes.
    If it does not divide cleanly, the new number is a prime as well.
**/
fn prime_sieve(n: i32) -> Vec<i32> {
    let mut primes = vec!(2);
    for x in 3..n {
        let mut prime = true;
        for p in &primes {
            if x % p == 0 {
                prime = false
            }
        }
        if prime == true {
            primes.push(x)
        }
    }
    return primes
}