fn main() {
    let lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let mut score = 0;
    for card in lines {
        let scratchcard: &str = card.split(": ").last().unwrap();

        let mut both_sides = scratchcard.split(" | ");
        let left_side: &str = both_sides.next().unwrap();
        let right_side: &str = both_sides.next().unwrap();

        let winning_numbers: Vec<u32> = left_side.split_whitespace().map(|num| num.parse().unwrap()).collect();
        let numbers_we_have: Vec<u32> = right_side.split_whitespace().map(|num| num.parse().unwrap()).collect();

        let matches: u32 = numbers_we_have.iter().fold(0, |acc, x| {
            if winning_numbers.contains(x) { acc + 1} else {acc}
        });

        let mut card_score = 0;
        if matches > 0 {
            card_score = 2u32.pow(matches - 1);
        }

        score += card_score;

        //println!("{:?}", matches);
        //println!("{:?}", card_score);
        //println!("{:?}", winning_numbers);
        //println!("{:?}\n", numbers_we_have);
    }
    println!("{}", score);
}
