use regex::Regex;

fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/example.txt").lines().collect();
    let string = lines.join("");
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let mut accumulator = 0;
    for (_, [num1, num2]) in re.captures_iter(&string).map(|c| c.extract()) {
        let num1 = num1.parse::<i32>().unwrap();
        let num2 = num2.parse::<i32>().unwrap();
        accumulator += num1 * num2;
    }
    println!("{:?}", accumulator);
}
