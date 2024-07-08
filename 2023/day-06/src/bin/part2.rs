#![allow(warnings)]

#[derive(Debug, Clone, Copy)]
struct Race {
    time: i64,
    distance_record: i64
}

fn main() {
    let time: i64 = 71530;
    let distance_record: i64 = 940200;
    let time: i64 = 56_97_78_75;
    let distance_record: i64 = 546_1927_1131_1139;

    let mut ways_to_beat_vec: Vec<i64> = Vec::new();
    let mut ways_to_beat: i64 = 0;
    for speed in 0..time {
        let remaining_time = time - speed;
        if remaining_time * speed > distance_record {
            ways_to_beat += 1;
        }
    }
    ways_to_beat_vec.push(ways_to_beat);

    dbg!(ways_to_beat_vec.iter().product::<i64>());
}