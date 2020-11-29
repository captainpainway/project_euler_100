// compile with rustc problem_6.rs
// run with ./problem_6

fn main() {
    println!("{}", diff(100));
    println!("{}", difference(100));
}

/**
    Using the formulas:
    sum_squares = (2n + 1)(n + 1)n / 6
    squared_sum = (n(n + 1) / 2) ^ 2
**/
fn difference(n: i32) -> i32 {
    let squared_sum = n * (n + 1) / 2;
    let sum_squares = (2 * n + 1) * (n + 1) * n / 6;
    squared_sum.pow(2) - sum_squares
}

// The naive implementation.
fn diff(n: i32) -> i32 {
    squared_sum(n) - sum_squares(n)
}

fn sum_squares(n: i32) -> i32 {
    (1..=n).map(|x| x.pow(2)).fold(0, |a, b| a + b)
}

fn squared_sum(n: i32) -> i32 {
    (1..=n).fold(0, |a, b| a + b).pow(2)
}