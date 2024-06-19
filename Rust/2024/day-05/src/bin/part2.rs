use num_format::{Locale, ToFormattedString};

fn parse_number_line(line: &str) -> Vec<u64> {
    line.split_whitespace().map(|num| num.parse().unwrap()).collect::<Vec<u64>>()
}

#[derive(Debug)]
struct Map {
    // looks like i didn't need these two below after all
    //source_name: String,
    //destination_name: String,
    mappings: Vec<Mapping>
}

#[derive(Debug)]
struct Mapping {
    source_start: u64,
	destination_start: u64,
    length: u64,
}

struct SeedMapping {
    start_range: u64,
    length: u64,
}

fn main() {
    let mut lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let unprocessed_seeds: Vec<u64> = parse_number_line(lines.remove(0).split("seeds: ").last().unwrap());


    let mut seeds_iter = unprocessed_seeds.iter();
    let mut seed_mappings: Vec<SeedMapping> = Vec::new();
    // for fun
    let mut sum: u64 = 0;
    while let Some(start_range) = seeds_iter.next() {
        let length = seeds_iter.next();
        sum += length.unwrap();
        seed_mappings.push(SeedMapping { start_range: *start_range, length: *length.unwrap() })
    }
    println!("Wow, that's a lot of seeds, more than 10: {:?}", sum);

    let mut master_garden_map: Vec<Map> = Vec::new();
    let mut unprocessed_master_garden_map: Vec<Vec<&str>> = Vec::new();
    for line in &lines {
        if line.is_empty() {
            master_garden_map.push(Map {mappings: Vec::new()});
            unprocessed_master_garden_map.push(Vec::new());
        } else if !line.chars().next().unwrap().is_numeric() {
           continue; 
        } else {
            unprocessed_master_garden_map.last_mut().unwrap().push(line);
        }
    }

    for (map_segment_index, map_segment) in unprocessed_master_garden_map.iter().enumerate() {
        for number_line in map_segment {
            let number_line_parsed = parse_number_line(&number_line);
            master_garden_map[map_segment_index].mappings.push(
                Mapping {
                    source_start: number_line_parsed[1],
                    destination_start: number_line_parsed[0],
                    length: number_line_parsed[2]
                })
            }
        }

    let mut lowest_location: u64 = u64::MAX;
    for seed_mapping in seed_mappings {
        for seed in (seed_mapping.start_range..(seed_mapping.start_range + seed_mapping.length)).step_by(50) {
            let mut current_key = seed;
            for map in &master_garden_map {
                for mapping in &map.mappings {
                    if (mapping.source_start..(mapping.source_start + mapping.length)).contains(&current_key) {
                        let difference = current_key - mapping.source_start;
                        current_key = mapping.destination_start + difference;
                        break;
                    }
                }
            }
            //println!("{}", current_key.to_formatted_string(&Locale::en));
            if lowest_location > current_key {
                lowest_location = current_key;
            }
        }
    }
    println!("{}", lowest_location);
}
