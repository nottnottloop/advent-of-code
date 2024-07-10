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
    let re = Regex::new(r"([A-Z][A-Z][A-Z]) = \(([A-Z][A-Z][A-Z]), ([A-Z][A-Z][A-Z])\)").unwrap();
    for line in &lines {
        let (_, [address, left, right]) = re.captures(&line).unwrap().extract();
        nodes.push(Node {
            address,
            left,
            right
        })
    }
    println!("{:?}", directions);
    println!("{:?}", &nodes);

    let mut move_count = 0;
    let mut direction_index = 0;
    let mut current_address: &str = "AAA";
    while current_address != "ZZZ" {
        for node in &nodes {
            if current_address == node.address {
                let current_direction = directions[direction_index];

                current_address = match current_direction {
                    'L' => node.left,
                    'R' => node.right,
                    _ => panic!()
                };

                move_count += 1;
                direction_index += 1;

                if current_address == "ZZZ" {
                    break;
                }

                if direction_index == directions.len() {
                    direction_index = 0;
                }
            }
        }
    }
    println!("{:?}", move_count);
}