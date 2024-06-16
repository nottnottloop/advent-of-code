fn main() {
    let lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let mut accumulator: u32 = 0;
    for game in lines {
        let game_slice: Vec<&str> = game.split(": ").collect();

        let iterations: Vec<&str> = game_slice[1].split("; ").collect();
        let mut highest_red = 0;
        let mut highest_green = 0;
        let mut highest_blue = 0;
        for iteration in &iterations {

            let colored_cube_slices: Vec<&str> = iteration.split(", ").collect();
            for cube_info in colored_cube_slices {
                let color_info: Vec<&str> = cube_info.split(" ").collect();
                let quantity: u32 = color_info[0].parse().unwrap();
                match color_info[1] {
                    "red" => if quantity > highest_red { highest_red = quantity },
                    "green" => if quantity > highest_green { highest_green = quantity },
                    "blue" => if quantity > highest_blue { highest_blue = quantity },
                    _ => panic!()
                }
            }
        }
        println!("Red: {highest_red} Green: {highest_green} Blue: {highest_blue}");
        accumulator += (highest_red * highest_green * highest_blue)
    }
    println!("{}", accumulator);
}