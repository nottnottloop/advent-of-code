use regex::Regex;

fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut counter = 0;
    for (y, line) in lines.iter().enumerate() {
        for (x, character) in line.chars().enumerate() {
            if character == 'A' {
                // H
                let mut top_left_c: char = 'H';
                let mut top_right_c: char = 'H';
                let mut bottom_left_c: char = 'H';
                let mut bottom_right_c: char = 'H';

                if let Some(upper_line) = lines.get(y.wrapping_sub(1)) {
                    if let Some(c) = upper_line.chars().nth(x.wrapping_sub(1)) {
                        top_left_c = c;
                    }
                    if let Some(c) = upper_line.chars().nth(x + 1) {
                        top_right_c = c;
                    }
                }

                if let Some(bottom_line) = lines.get(y + 1) {
                    if let Some(c) = bottom_line.chars().nth(x.wrapping_sub(1)) {
                        bottom_left_c = c;
                    }
                    if let Some(c) = bottom_line.chars().nth(x + 1) {
                        bottom_right_c = c;
                    }
                }
                let tl_to_br = String::from(format!("{}{}{}", top_left_c, 'A', bottom_right_c));
                let bl_to_tr = String::from(format!("{}{}{}", bottom_left_c, 'A', top_right_c));
                if (tl_to_br == "SAM" || tl_to_br == "MAS") && (bl_to_tr == "SAM" || bl_to_tr == "MAS") {
                    counter += 1;
                }
            }
        }
    }
    println!("{:?}", counter);
}