fn parse_number_line(line: &str) -> Vec<u64> {
    line.split_whitespace().map(|num| num.parse().unwrap()).collect::<Vec<u64>>()
}

#[derive(Debug)]
struct Map {
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

fn main() {
    let mut lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let seeds: Vec<u64> = parse_number_line(lines.remove(0).split("seeds: ").last().unwrap());

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
    //println!("{:?}", unprocessed_master_garden_map);

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

    let mut locations: Vec<u64> = Vec::new();
    for seed in seeds {
        let mut current_key = seed;
        for map in &master_garden_map {
            for mapping in &map.mappings {
                if (mapping.source_start..(mapping.source_start + mapping.length)).contains(&current_key) {
                    // vietnam
                    let difference = current_key - mapping.source_start;
                    //if seed == 14 {
                    //    dbg!(difference, current_key, mapping.source_start, mapping.destination_start);
                    //    println!("");
                    //}
                    current_key = mapping.destination_start + difference;
                    // the break statement that could have saved much time
                    // without this break statement, it's like pretending that
                    // the next map is just another mapping within the same map
                    break;
                }
            }
        }
        locations.push(current_key);
    }
    //dbg!(master_garden_map);
    println!("{:?}", locations);
    println!("{:?}", locations.iter().min().unwrap());
}
