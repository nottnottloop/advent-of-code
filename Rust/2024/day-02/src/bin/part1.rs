fn main() {
    const RED_CUBE_LIMIT: u32 = 12;
    const GREEN_CUBE_LIMIT: u32 = 13;
    const BLUE_CUBE_LIMIT: u32 = 14;

    let lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let mut accumulator: u32 = 0;
    for game in lines {
        let game_slice: Vec<&str> = game.split(": ").collect();
        let game_num: u32 = game_slice[0].split(" ").collect::<Vec<&str>>()[1].parse().unwrap();
        let mut condemn_this_game = false;

        let iterations: Vec<&str> = game_slice[1].split("; ").collect();
        for iteration in &iterations {
            let mut red_count = 0;
            let mut green_count = 0;
            let mut blue_count = 0;

            let colored_cube_slices: Vec<&str> = iteration.split(", ").collect();
            for cube_info in colored_cube_slices {
                let color_info: Vec<&str> = cube_info.split(" ").collect();
                let quantity: u32 = color_info[0].parse().unwrap();
                match color_info[1] {
                    "red" => red_count += quantity,
                    "green" => green_count += quantity,
                    "blue" => blue_count += quantity,
                    _ => panic!()
                }
            }
            if red_count > RED_CUBE_LIMIT || green_count > GREEN_CUBE_LIMIT || blue_count > BLUE_CUBE_LIMIT {
                condemn_this_game = true;
            }
        }
        if !condemn_this_game {
            accumulator += game_num;
        }
    }
    println!("{}", accumulator);
}