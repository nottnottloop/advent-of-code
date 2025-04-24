fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for line in lines {
        let test: Vec<&str> = line.split_whitespace().collect();
        left.push(test[0].parse().unwrap());
        right.push(test[1].parse().unwrap());
    }
    let mut accumulator = 0;
    for num in left {
        let appearances_in_right: i32 = right.iter().filter(|&&x| x == num).count() as i32;
        let result = num * appearances_in_right;
        println!("{}", result);
        accumulator += result;
    }
    println!("{:?}", accumulator);
}
