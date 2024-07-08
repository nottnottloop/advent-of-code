#![allow(warnings)]

#[derive(Debug, Clone, Copy)]
struct Race {
    time: i64,
    distance_record: i64
}

fn main() {
    let lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();

    let mut times: Vec<&str> = lines[0].split_whitespace().collect();
    let mut distance_records: Vec<&str> = lines[1].split_whitespace().collect();
    times.remove(0);
    distance_records.remove(0);
    let times: Vec<i64> = times.iter().map(|x| x.parse::<i64>().unwrap()).collect();
    let distance_records: Vec<i64> = distance_records.iter().map(|x| x.parse::<i64>().unwrap()).collect();
    let mut races: Vec<Race> = Vec::new();
    for i in 0..times.len() {
        races.push(Race {time: times[i], distance_record: distance_records[i]});
    }

    dbg!(&races);

    let mut ways_to_beat_vec: Vec<i64> = Vec::new();
    for race in &races {
        let mut ways_to_beat: i64 = 0;
        for speed in 0..race.time {
            let remaining_time = race.time - speed;
            if remaining_time * speed > race.distance_record {
                ways_to_beat += 1;
            }
        }
        ways_to_beat_vec.push(ways_to_beat);
    }

    dbg!(ways_to_beat_vec.iter().product::<i64>());
}