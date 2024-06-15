fn main() {
    let str = include_str!("part_1.txt");

    let lines: Vec<&str> = str.split("\n").collect();
    let mut values: Vec<u32> = Vec::new();

    println!("{:?}", lines);

    for line in lines {
        let mut count = 0;
        let mut first_char = ' ';
        let mut last_char = ' ';

        for char in line.chars() {
            if !char.is_numeric() { continue; }
            if count == 0 {
                first_char = char;
            } else {
                last_char = char;
            }
            count += 1;
        }

        let mut string = String::new();
        if count == 1 {
            string.push(first_char);
            string.push(first_char);
        } else {
            string.push(first_char);
            string.push(last_char);
        }
        values.push(string.parse::<u32>().unwrap());
    }

    println!("{:?}", values);
    println!("{:?}", values.iter().sum::<u32>());
}
