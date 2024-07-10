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
            right
        })
    }
    //println!("{:?}", directions);
    //println!("{:?}", &nodes);

    let mut move_count = 0;
    let mut direction_index = 0;
    let mut current_addresses: Vec<&Node> = nodes.iter().filter(|node| node.address.chars().last().unwrap() == 'A').collect();
    let starting_address_count = current_addresses.len();
    loop {
        let mut new_current_addresses: Vec<&Node> = Vec::new();
        let current_direction = directions[direction_index];
        for current_address in &current_addresses {
            let node = nodes.iter().find(|node| node.address == current_address.address).unwrap();
            let new_current_address = match current_direction {
                'L' => node.left,
                'R' => node.right,
                _ => panic!()
            };
            let node = nodes.iter().find(|node| node.address == new_current_address).unwrap();
            new_current_addresses.push(node);
        }
        

        let are_we_there_yet: Vec<&&Node> = new_current_addresses.iter().filter(|node| node.address.chars().last().unwrap() == 'Z').collect();

        if are_we_there_yet.len() > 2 {
            //dbg!(&starting_address_count); (6)
            dbg!(&are_we_there_yet.len());
        }
        //if move_count == 1000 {
        //    dbg!(&current_addresses);
        //    dbg!(&new_current_addresses);
        //    dbg!(&starting_address_count);
        //}

        move_count += 1;
        direction_index += 1;
        if direction_index == directions.len() {
            direction_index = 0;
        }
        if starting_address_count == are_we_there_yet.len() {
            break;
        }

        current_addresses = new_current_addresses;
    }
    println!("{:?}", move_count);
}