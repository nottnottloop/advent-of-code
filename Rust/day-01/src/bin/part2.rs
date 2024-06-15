fn return_relevant_char(str: &str) -> char {
    match str {
        "1" | "one" => '1',
        "2" | "two" => '2',
        "3" | "three" => '3',
        "4" | "four" => '4',
        "5" | "five" => '5',
        "6" | "six" => '6',
        "7" | "seven" => '7',
        "8" | "eight" => '8',
        "9" | "nine" => '9',
        _ => panic!()
    }
}

fn main() {
    let str = include_str!("part_1.txt");

    let lines: Vec<&str> = str.split("\n").collect();
    let mut values: Vec<u32> = Vec::new();
    const NUMBER_STRS: &[&str] = &["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    for line in lines {
        let mut arr: Vec<(usize, &str)> = Vec::new();
        for str in NUMBER_STRS {
            let num_arr: Vec<(usize, &str)> = line.match_indices(str).collect();
            if !num_arr.is_empty() {
                arr.extend(num_arr);
            }
        }

        arr.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

        let first_char = return_relevant_char(arr.first().unwrap().1);
        let last_char = return_relevant_char(arr.last().unwrap().1);
        
        let mut string = String::new();
        string.push(first_char);
        string.push(last_char);
        values.push(string.parse::<u32>().unwrap());
    }

    println!("{:?}", values);
    println!("{:?}", values.iter().sum::<u32>());
}
