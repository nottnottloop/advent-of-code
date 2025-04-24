use regex::Regex;

fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let string = lines.join("");
    let mul_regex = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let do_regex = Regex::new(r"(do\(\))").unwrap();
    let dont_regex = Regex::new(r"(don't\(\))").unwrap();

    let mut mul_instructions: Vec<_> = Vec::new();
    let mut dos: Vec<_> = Vec::new();
    let mut donts: Vec<_> = Vec::new();
    for mul_instruction in mul_regex.captures_iter(&string) {
        mul_instructions.push(mul_instruction);
    }
    for do_instruction in do_regex.captures_iter(&string) {
        dos.push(do_instruction);
    }
    for dont_instruction in dont_regex.captures_iter(&string) {
        donts.push(dont_instruction);
    }

    let mut instructions_enabled_table = vec![true; string.len()];
    for index in 0..instructions_enabled_table.len() {
        for do_instruction in &dos {
            if do_instruction.get(0).unwrap().start() == index {
                for val in &mut instructions_enabled_table[index..] {
                    *val = true;
                }
            }
        }
        for dont_instruction in &donts {
            if dont_instruction.get(0).unwrap().start() == index {
                for val in &mut instructions_enabled_table[index..] {
                    *val = false;
                }
            }
        }
    }
    let mut accumulator = 0;
    for mul_instruction in mul_regex.captures_iter(&string) {
        let start_pos = mul_instruction.get(0).unwrap().start();
        if instructions_enabled_table[start_pos] {
            let num1 = mul_instruction.get(1).unwrap().as_str().parse::<i32>().unwrap();
            let num2 = mul_instruction.get(2).unwrap().as_str().parse::<i32>().unwrap();
            accumulator += num1 * num2;
        }
    }
    println!("{:?}", accumulator);
}
