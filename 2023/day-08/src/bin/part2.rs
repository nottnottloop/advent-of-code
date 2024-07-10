#![allow(warnings)]

use regex::Regex;
#[derive(Debug, Clone, Copy)]
struct Node {
    address: &'static str,
    left: &'static str,
    right: &'static str,
}
fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let directions: Vec<char> = lines.remove(0).chars().collect();
    lines.remove(0);

    let mut nodes: Vec<Node> = Vec::new();
    let re = Regex::new(r"(...) = \((...), (...)\)").unwrap();
    for line in &lines {
        let (_, [address, left, right]) = re.captures(&line).unwrap().extract();
        nodes.push(Node {
            address,
            left,
            right,
        })
    }
    //println!("{:?}", directions);
    //println!("{:?}", &nodes);

    let mut start_addresses: Vec<&Node> = nodes
        .iter()
        .filter(|node| node.address.chars().last().unwrap() == 'A')
        .collect();
    let mut move_counts: Vec<u64> = Vec::new();
    for address_start in &start_addresses {
        let mut move_count = 0;
        let mut direction_index = 0;
        let mut current_address = address_start.address;
        loop {
            let current_direction = directions[direction_index];
            let node = nodes
                .iter()
                .find(|node| node.address == current_address)
                .unwrap();
            current_address = match current_direction {
                'L' => node.left,
                'R' => node.right,
                _ => panic!(),
            };
            let node = nodes
                .iter()
                .find(|node| node.address == current_address)
                .unwrap();

            move_count += 1;
            direction_index += 1;
            if direction_index == directions.len() {
                direction_index = 0;
            }

            if current_address.chars().last().unwrap() == 'Z' {
                move_counts.push(move_count);
                break;
            }
        }
    }

    println!("{:?}", move_counts);
    println!("{:?}", lcm_multiple(move_counts));
}

// chatgpt
fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: u64, b: u64) -> u64 {
    a * b / gcd(a, b)
}

fn lcm_multiple(numbers: Vec<u64>) -> u64 {
    numbers.iter().cloned().reduce(lcm).unwrap_or(1)
}