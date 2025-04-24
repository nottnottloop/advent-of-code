fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for line in lines {
        let test: Vec<&str> = line.split_whitespace().collect();
        left.push(test[0].parse().unwrap());
        right.push(test[1].parse().unwrap());
    }
    left.sort();
    right.sort();
    let arr: Vec<_> = left.iter().zip(right.iter()).collect();
    let mut accumulator = 0;
    for element in arr {
        let result = element.0.abs_diff(*element.1);
        accumulator += result;
    }
    println!("{:?}", accumulator);
}
