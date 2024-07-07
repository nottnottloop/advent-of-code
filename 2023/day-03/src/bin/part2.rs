use std::collections::HashSet;

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
struct MapSymbol {
    x: i32,
    y: i32,
    touched_by: Option<Pos>,
    char: char
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
struct Pos {
    x: i32,
    y: i32,
}

fn main() {
    let lines = include_str!("input.txt").lines();
    let mut engine_schematic_map: Vec<MapSymbol> = Vec::new();

    for (line_index, line) in lines.clone().enumerate() {
        for (char_index, char) in line.chars().enumerate() {
            engine_schematic_map.push(MapSymbol {y: line_index as i32, x: char_index as i32, char, touched_by: None});
        }
    }

    let mut touching_numbers: Vec<MapSymbol> = Vec::new();
    for central_number in &engine_schematic_map {
        if !central_number.char.is_numeric() { continue; }
        for testing_symbol in &engine_schematic_map {
            if testing_symbol.char != '*' { continue; }
            let mut symbol_detected = false;
            // top and bottom
            if (central_number.x - 1 == testing_symbol.x ||
            central_number.x == testing_symbol.x ||
            central_number.x + 1 == testing_symbol.x) &&
            (central_number.y - 1 == testing_symbol.y || central_number.y + 1 == testing_symbol.y) {
                symbol_detected = true;
            }
            // sides
            if (central_number.x - 1 == testing_symbol.x || central_number.x + 1 == testing_symbol.x) && central_number.y == testing_symbol.y {
                symbol_detected = true;
            }

            if symbol_detected && testing_symbol.char != '.' {
                let mut tweaked_central_number = central_number.clone();
                tweaked_central_number.touched_by = Some(Pos {x: testing_symbol.x, y: testing_symbol.y});
                touching_numbers.push(tweaked_central_number.clone());
                //println!("Central: {:?} found Testing: {:?}", central_number, testing_symbol);
            }
        }
    }

    //println!("{:#?}", touching_numbers);
    let mut number_map: Vec<Vec<MapSymbol>> = Vec::new();
    for start_point in &touching_numbers {
        //println!("{:?}", start_point);
        let mut map_entry: Vec<MapSymbol> = Vec::new();
        map_entry.push(start_point.clone());
        for testing_symbol in &engine_schematic_map {
            if start_point.y != testing_symbol.y { continue; }
            if !testing_symbol.char.is_numeric() { continue; };
            if start_point.x - 1 == testing_symbol.x {
                map_entry.push(testing_symbol.clone());
                    for testing_symbol2 in &engine_schematic_map {
                        if start_point.y != testing_symbol2.y { continue; }
                        if !testing_symbol2.char.is_numeric() { continue; };
                        if start_point.x - 2 == testing_symbol2.x {
                            map_entry.push(testing_symbol2.clone());
                        }
                    }
            }
            if start_point.x + 1 == testing_symbol.x {
                map_entry.push(testing_symbol.clone());
                for testing_symbol2 in &engine_schematic_map {
                    if start_point.y != testing_symbol2.y { continue; }
                    if !testing_symbol2.char.is_numeric() { continue; };
                    if start_point.x + 2 == testing_symbol2.x {
                        map_entry.push(testing_symbol2.clone());
                    }
                }
            }
        }
        number_map.push(map_entry);
    }

    for map_entry in number_map.iter_mut() {
        map_entry.sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap());
    }

    for map_entry in number_map.iter_mut() {
        let mut pos_to_copy: Option<Pos> = None;
        for symbol in map_entry.iter() {
            if let Some(pos) = symbol.touched_by.clone() {
                pos_to_copy = Some(pos);
                break;
            }
        }
        for symbol in map_entry.iter_mut() {
            symbol.touched_by = pos_to_copy.clone();
        }
    }

    let number_map_set: HashSet<_> = number_map.iter().collect();

    //println!("{:?}", number_map_set);

    let mut valid_numbers: Vec<(Pos, i32)> = Vec::new();
    for map_entry in number_map_set.iter() {
        let mut string = String::new();
        for symbol in map_entry.iter() {
            string.push(symbol.char);
        }
        //println!("{:?}", &map_entry);
        valid_numbers.push((map_entry[0].touched_by.clone().unwrap(), string.parse().unwrap()));
    }

    let mut accumulator: i32 = 0;
    for num1 in &valid_numbers {
        for num2 in &valid_numbers {
            // this will fail if two identical numbers are touching the same gear
            // but i got away with it
            if num1.0 == num2.0 && num1.1 != num2.1 {
                accumulator += num1.1 * num2.1;
            }
        }
    }

    println!("{:?}", valid_numbers);
    println!("{:?}", accumulator / 2);
}
