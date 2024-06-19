use std::collections::HashMap;

fn parse_number_line(line: &str) -> Vec<u64> {
    line.split_whitespace().map(|num| num.parse().unwrap()).collect::<Vec<u64>>()
}

#[derive(Debug)]
struct Map {
    //source_name: String,
    //destination_name: String,
    conversion_map: Option<HashMap<u64, u64>>
}

fn main() {
    let mut lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let seeds: Vec<u64> = parse_number_line(lines.remove(0).split("seeds: ").last().unwrap());

    let mut master_garden_map: Vec<Map> = Vec::new();
    let mut unprocessed_master_garden_map: Vec<Vec<&str>> = Vec::new();
    for line in &lines {
        if line.is_empty() {
            master_garden_map.push(Map {conversion_map: None});
            unprocessed_master_garden_map.push(Vec::new());
        } else if !line.chars().next().unwrap().is_numeric() {
           continue; 
        } else {
            unprocessed_master_garden_map.last_mut().unwrap().push(line);
        }
    }

    for (map_segment_index, map_segment) in unprocessed_master_garden_map.iter().enumerate() {
        let mut conversion_map: HashMap<u64, u64> = HashMap::new();
        for mapping in map_segment {
            let number_line = parse_number_line(&mapping);
            let (destination_start, source_start, length) = (number_line[0], number_line[1], number_line[2]);

            // this gobbles memory holy crap
            let source_values: Vec<u64> = (source_start..(source_start + length)).collect();
            let destination_values: Vec<u64> = (destination_start..(destination_start + length)).collect();

        
            for (source_value, destination_value) in source_values.iter().zip(destination_values.iter()) {
                conversion_map.insert(source_value.clone(), destination_value.clone());
            }
        }
        master_garden_map[map_segment_index].conversion_map = Some(conversion_map);
    }

    let mut locations: Vec<u64> = Vec::new();
    for seed in seeds {
        let mut current_key = seed;
        for current_map in &master_garden_map {
            current_key = *current_map.conversion_map.as_ref().unwrap().get(&current_key).unwrap_or(&current_key);
        }
        locations.push(current_key);
    }
    println!("{:?}", locations);
    println!("{:?}", locations.iter().min().unwrap());
}
