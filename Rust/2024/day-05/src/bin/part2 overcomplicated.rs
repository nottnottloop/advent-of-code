#![allow(clippy::never_loop)]
use std::ops::Range;
use std::cmp::{min, max};
use num_format::{Locale, ToFormattedString};

fn ranges_overlap(range1: &Range<i64>, range2: &Range<i64>) -> bool {
    range1.start < range2.end && range2.start < range1.end
}

fn parse_number_line(line: &str) -> Vec<i64> {
    line.split_whitespace().map(|num| num.parse().unwrap()).collect::<Vec<i64>>()
}

//#[derive(Debug)]
//struct Map {
//    // looks like i didn't need these two below after all
//    //source_name: String,
//    //destination_name: String,
//    mappings: Vec<Mapping>
//}

#[derive(Debug)]
struct Mapping {
    source_range: Range<i64>,
    destination_range: Range<i64>,
    length: i64
}

fn main() {
    let mut lines: Vec<&str> = include_str!("example.txt").lines().collect();
    let unprocessed_seeds: Vec<i64> = parse_number_line(lines.remove(0).split("seeds: ").last().unwrap());

    let mut seeds_iter = unprocessed_seeds.iter();
    let mut seed_mappings: Vec<Mapping> = Vec::new();
    // for fun
    let mut sum: i64 = 0;
    while let Some(start_range) = seeds_iter.next() {
        let length = seeds_iter.next();
        sum += length.unwrap();
        seed_mappings.push(Mapping { source_range: 0..0, destination_range: *start_range..(*start_range + *length.unwrap()), length: *length.unwrap() })
    }
    println!("Wow, that's a lot of seeds, more than 10: {:?}", sum);

    let mut master_garden_map: Vec<Vec<Option<Mapping>>> = Vec::new();
    let mut unprocessed_master_garden_map: Vec<Vec<&str>> = Vec::new();
    for line in &lines {
        if line.is_empty() {
            master_garden_map.push(Vec::new());
            unprocessed_master_garden_map.push(Vec::new());
        } else if !line.chars().next().unwrap().is_numeric() {
           continue; 
        } else {
            unprocessed_master_garden_map.last_mut().unwrap().push(line);
        }
    }

    //dbg!(&unprocessed_master_garden_map);
    for (map_segment_index, map_segment) in unprocessed_master_garden_map.iter().enumerate() {
        let mut new_mappings: Vec<Option<Mapping>> = Vec::new();
        for number_line in map_segment {
            let number_line_parsed = parse_number_line(number_line);
            new_mappings.push(
                Some(Mapping {
                    source_range: (number_line_parsed[1]..(number_line_parsed[1] + number_line_parsed[2])),
                    destination_range: (number_line_parsed[0]..(number_line_parsed[0] + number_line_parsed[2])),
                    length: number_line_parsed[2]
                }))
        }
        master_garden_map[map_segment_index] = new_mappings;
    }
    //dbg!(&master_garden_map);

    let mut lowest_location = i64::MAX;
    for (seed_index, seed_mapping) in seed_mappings.iter().enumerate() {
        if seed_index != 0 {
            println!("{}", "I'm out");
            std::process::exit(0);
        }
        //let mut current_number: i64 = seed_range.start;
        // will contain every possible range for each map for a seed
        let mut range_objects: Vec<Vec<Option<Mapping>>> = Vec::new();
        let mut ranges_to_enter_with: Vec<Range<i64>> = vec![seed_mapping.destination_range.clone()];
        let mut next_ranges_to_enter_with: Vec<Range<i64>> = Vec::new();
        for (map_index, map) in master_garden_map.iter().enumerate() {
            range_objects.push(Vec::new());
            for entering_range in &ranges_to_enter_with {
                let mut ranges_overlapped = false;
                for mapped_ranges in map {
                    let source_range = &mapped_ranges.as_ref().unwrap().source_range;
                    let destination_range = &mapped_ranges.as_ref().unwrap().destination_range;
                    //dbg!(entering_range, source_range);
                    if ranges_overlap(entering_range, source_range) {
                        ranges_overlapped = true;
                        if entering_range.start < source_range.start {
                            next_ranges_to_enter_with.push(entering_range.start..source_range.start);
                        }
                        if entering_range.end > source_range.end {
                            next_ranges_to_enter_with.push(source_range.end..entering_range.end);
                        }
                        // figure out the exact points to make and exclusive range
                        // that applies to both ranges
                        let new_source_range_start = max(entering_range.start, source_range.start);
                        let new_source_range_end = min(entering_range.end, source_range.end);
                        let difference = destination_range.start - source_range.start;
                        let new_destination_range = (new_source_range_start + difference)..(new_source_range_end + difference);
                        range_objects[map_index].push(
                            Some(Mapping {
                                source_range: new_source_range_start..new_source_range_end,
                                destination_range: new_destination_range.clone(),
                                length: (new_source_range_end - new_source_range_start).abs()
                            })
                        );
                        next_ranges_to_enter_with.push(new_destination_range.clone());
                    }
                }
                if !ranges_overlapped {
                    next_ranges_to_enter_with.push(entering_range.clone());
                    range_objects[map_index].push(
                        Some(Mapping {
                            source_range: entering_range.clone(),
                            destination_range: entering_range.clone(),
                            length: 42
                        })
                    );
                    println!("No overlap, adding {entering_range:?} to next_ranges_to_enter_with");
                }
            }
            //dbg!(&range_objects[map_index]);
            dbg!(&ranges_to_enter_with);
            //dbg!(&next_ranges_to_enter_with);
            ranges_to_enter_with = next_ranges_to_enter_with.clone(); next_ranges_to_enter_with.clear();
        }
        //std::process::exit(0);

        //let mut iter = current_range_objects.iter();
        //while let Some(range_object) = iter.next() {

        //}


        
        //if current_number < lowest_location {
        //    lowest_location = current_number;
        //}
    }
    println!("{}", lowest_location);
}
                //    let difference = source_range.start - destination_range.start;
                //    //dbg!(difference, current_number, source_range, destination_range);
                //    //println!("");
                //    current_number = destination_range.start - difference;
                //    break;
