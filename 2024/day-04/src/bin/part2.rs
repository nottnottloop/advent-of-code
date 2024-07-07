use std::collections::HashMap;
use regex::Regex;

fn main() {
    let lines: Vec<&str> = include_str!("input.txt").lines().collect();
    let mut scratchcard_bible: HashMap<u32, u32> = HashMap::new();
    let re = Regex::new(r"Card\s+(?<num>\d+)").unwrap();
    for original_cards in lines {
        let mut card_information = original_cards.split(": ");
        //println!("{:?}", card_information.next());
        let id: u32 = re.captures(card_information.next().unwrap()).unwrap().get(1).unwrap().as_str().parse().unwrap();

        let mut both_sides = card_information.next().unwrap().split(" | ");
        let left_side: &str = both_sides.next().unwrap();
        let right_side: &str = both_sides.next().unwrap();

        let winning_numbers: Vec<u32> = left_side.split_whitespace().map(|num| num.parse().unwrap()).collect();
        let numbers_we_have: Vec<u32> = right_side.split_whitespace().map(|num| num.parse().unwrap()).collect();

        let matches: u32 = numbers_we_have.iter().fold(0, |acc, x| {
            if winning_numbers.contains(x) { acc + 1} else {acc}
        });
        scratchcard_bible.insert(id, matches);
    }

    let mut scratchcard_count = 0;
    let mut scratchcard_stack: Vec<u32> = (1..=scratchcard_bible.len() as u32).collect();

    while let Some(id) = scratchcard_stack.pop() {
        scratchcard_count += 1;
        let end_range_of_cards_to_win = id + scratchcard_bible[&id];
        let new_scratchcards: Vec<u32> = ((id + 1)..=end_range_of_cards_to_win).collect();
        scratchcard_stack.extend(new_scratchcards);
        //println!("{:?}", scratchcard_stack);
    }
    println!("{}", scratchcard_count);
}