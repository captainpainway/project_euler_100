// compile with rustc problem_4.rs
// run as ./problem_4

fn main() {
    let mut a = 999;
    let mut largest = 0;
    loop {
        let mut b = 999;
        if &a * b < largest {
            break;
        }
        loop {
            if b < 100 {
                break
            }
            if get_palindrome(&a * &b) && &a * &b > largest {
                largest = &a * &b;
            }
            b -= 1;
        }
        a -= 1;
    }
    println!("{}", largest);
}

fn get_palindrome(n: i32) -> bool {
    let v = n.to_string()
        .chars()
        .rev()
        .into_iter()
        .collect::<String>()
        .parse::<i32>()
        .unwrap();
    v == n
}