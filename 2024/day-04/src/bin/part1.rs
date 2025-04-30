use regex::Regex;

fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut xmas_map: Vec<String> = Vec::new();
    for (y, line) in lines.iter().enumerate() {
        for (x, character) in line.chars().enumerate() {
            if character == 'X' {
                // Right
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(c) = line.chars().nth(x + i) {
                        chars.push(c);
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "right");
                // Left
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(c) = line.chars().nth(x.wrapping_sub(i)) {
                        chars.push(c);
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "left");
                // Up
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y.wrapping_sub(i)) {
                        if let Some(c) = check_line.chars().nth(x) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "up");
                // Down
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y + i) {
                        if let Some(c) = check_line.chars().nth(x) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "down");
                // Top right
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y.wrapping_sub(i)) {
                        if let Some(c) = check_line.chars().nth(x + i) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "top right");
                // Bottom right
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y + i) {
                        if let Some(c) = check_line.chars().nth(x + i) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "bottom right");
                // Top left
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y.wrapping_sub(i)) {
                        if let Some(c) = check_line.chars().nth(x.wrapping_sub(i)) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "top left");
                // Bottom left
                let mut chars: String = String::new();
                for i in 0..4 {
                    if let Some(check_line) = lines.get(y + i) {
                        if let Some(c) = check_line.chars().nth(x.wrapping_sub(i)) {
                            chars.push(c);
                        }
                    } else {
                        break;
                    }
                }
                add_to_map(&mut xmas_map, chars, x, y, "bottom left");
            }
        }
    }
    println!("{:?}", xmas_map);
    println!("{:?}", xmas_map.len());
    println!("{:?}", xmas_map.iter().filter(|&s| s == "XMAS").count());
}

fn add_to_map(map: &mut Vec<String>, string: String, x: usize, y: usize, method: &str) {
    if string == "XMAS" {
        println!("x: {}, y: {}, method: {}", x, y, method);
        map.push(string);
    }
}
