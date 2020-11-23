// compile with rustc problem_3.rs
// run as ./problem_3

fn main() {
    println!("{}", faster_largest_prime(13195));
    println!("{}", faster_largest_prime(600851475143));
}

fn faster_largest_prime(mut n: i64) -> i64 {
    let mut factor = 2;
    let mut last_factor = 1;
    loop {
        if n == 1 {
            return last_factor;
        }
        if n % factor == 0 {
            last_factor = factor;
            n = n / factor;
        } else {
            factor += 1;
        }
    }
}