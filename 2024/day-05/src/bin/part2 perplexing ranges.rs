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

#[derive(Debug, Clone)]
struct Mapping {
    source_range: Range<i64>,
    destination_range: Range<i64>,
    difference: i64,
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
        seed_mappings.push(Mapping { difference: 0, source_range: 0..0, destination_range: *start_range..(*start_range + *length.unwrap())})
    }
    println!("Wow, that's a lot of seeds, more than 10: {:?}", sum);

    let mut master_garden_map: Vec<Vec<Mapping>> = Vec::new();
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
        let mut new_mappings: Vec<Mapping> = Vec::new();
        let mut start_of_mappings: i64 = i64::MAX;
        let mut end_of_mappings: i64 = i64::MIN;
        for number_line in map_segment {
            let number_line_parsed = parse_number_line(number_line);
            new_mappings.push(
                Mapping {
                    source_range: (number_line_parsed[1]..(number_line_parsed[1] + number_line_parsed[2])),
                    destination_range: (number_line_parsed[0]..(number_line_parsed[0] + number_line_parsed[2])),
                    difference: number_line_parsed[0] - number_line_parsed[1],
                });
            if number_line_parsed[1] < start_of_mappings {
                start_of_mappings = number_line_parsed[1]
            }
            if number_line_parsed[1] + number_line_parsed[2] > end_of_mappings {
                end_of_mappings = number_line_parsed[1] + number_line_parsed[2]
            }
        }
        master_garden_map[map_segment_index] = new_mappings;
    }
    dbg!(&master_garden_map);
    dbg!(&master_garden_map.len());

    let mut new_mappings: Vec<Mapping> = Vec::new();
    while master_garden_map.len() != 1 {
        let second_mappings = master_garden_map.pop().unwrap();
        let first_mappings = master_garden_map.pop().unwrap();
        for first_mapping in &first_mappings {
            for second_mapping in &second_mappings {
                if ranges_overlap(&first_mapping.destination_range, &second_mapping.source_range) {
                    // fully overlapping
                    if first_mapping.destination_range.start > second_mapping.source_range.start
                    && first_mapping.destination_range.end < second_mapping.source_range.end {
                        new_mappings.push(Mapping {
                            source_range: (second_mapping.source_range.start - first_mapping.difference)..(second_mapping.source_range.end - first_mapping.difference),
                            destination_range: (first_mapping.destination_range.start + second_mapping.difference)..(first_mapping.destination_range.end + second_mapping.difference),
                            difference: first_mapping.difference + second_mapping.difference,
                        });
                    }

                    // first map destination range starts lower than second map source range
                    // finishing inside of second map source range
                    else if first_mapping.destination_range.start < second_mapping.source_range.start
                    && first_mapping.destination_range.end < second_mapping.source_range.end {
                        // transformation outside the second map source range (maintain initial transformation)
                        new_mappings.push(Mapping {
                            source_range: first_mapping.source_range.start..(second_mapping.source_range.start - first_mapping.difference),
                            destination_range: first_mapping.destination_range.start..(second_mapping.source_range.start + first_mapping.difference),
                            difference: first_mapping.difference,
                        });
                        // both transformations inside the second map source range
                        new_mappings.push(Mapping {
                            source_range: (second_mapping.source_range.start - first_mapping.difference)..(second_mapping.source_range.end - first_mapping.difference),
                            destination_range: (first_mapping.destination_range.start + second_mapping.difference)..(first_mapping.destination_range.end + second_mapping.difference),
                            difference: first_mapping.difference + second_mapping.difference,
                        });
                    }

                    // first map destination range starts inside the second map source range
                    // finishing outside of second map source range
                    else if first_mapping.destination_range.start > second_mapping.source_range.start
                    && first_mapping.destination_range.end > second_mapping.source_range.end {
                        // transformation outside the second map source range (maintain initial transformation)
                        new_mappings.push(Mapping {
                            source_range: (second_mapping.source_range.end - first_mapping.difference)..first_mapping.source_range.end,
                            destination_range: (second_mapping.source_range.end + first_mapping.difference)..first_mapping.destination_range.end,
                            difference: first_mapping.difference,
                        });
                        // both transformations inside the second map source range
                        new_mappings.push(Mapping {
                            source_range: (second_mapping.source_range.start - first_mapping.difference)..(second_mapping.source_range.end - first_mapping.difference),
                            destination_range: (first_mapping.destination_range.start + second_mapping.difference)..(first_mapping.destination_range.end + second_mapping.difference),
                            difference: first_mapping.difference + second_mapping.difference,
                        });
                    }

                } else {
                    new_mappings.push(first_mapping.clone());
                    break;
                }
            }
        }
    }

    dbg!(&new_mappings);
    dbg!(&new_mappings.len());

    let mut lowest_location = i64::MAX;
    for seed_mapping in seed_mappings {
        let mut range = seed_mapping.destination_range;
        for (map_index, map) in master_garden_map.iter().enumerate() {

        }

        //let mut iter = current_range_objects.iter();
        //while let Some(range_object) = iter.next() {

        //}


        
        //if current_number < lowest_location {
        //    lowest_location = current_number;
        //}
    }
    //if ranges_overlap(&(5i64..11i64), &(2i64..6i64)) {
    //    println!("{}", "adsfsadf");
    //}
    println!("{}", lowest_location);
}
                //    let difference = source_range.start - destination_range.start;
                //    //dbg!(difference, current_number, source_range, destination_range);
                //    //println!("");
                //    current_number = destination_range.start - difference;
                //    break;
