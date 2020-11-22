// compile with rustc problem_2.rs
// run as ./problem_2

fn main() {
    let limit = 4000000;
    let mut a = 1;
    let mut b = 2;
    let mut vec: Vec<i32> = vec![a, b];
    loop {
        let c = &a + &b;
        a = b;
        b = c;
        if c >= limit {
            let sum: i32 = vec.into_iter().filter(|&x| x % 2 == 0).sum();
            println!("{:?}", sum);
            break;
        }
        vec.push(c);
    }
}