#![allow(warnings)]

use std::collections::HashMap;

#[derive(Debug, Copy, Clone)]
struct Hand {
    cards: &'static str,
    bid: i64,
    hand_type: &'static str,
}

fn get_hand_type_rank(hand_type: &str) -> i64 {
    match hand_type {
        "FiveOfAKind" => 6,
        "FourOfAKind" => 5,
        "FullHouse" => 4,
        "ThreeOfAKind" => 3,
        "TwoPair" => 2,
        "OnePair" => 1,
        "HighCard" => 0,
        _ => panic!()
    }
}

fn get_card_value(card: char) -> i64 {
    match card {
        '2' => 2,
        '3' => 3,
        '4' => 4,
        '5' => 5,
        '6' => 6,
        '7' => 7,
        '8' => 8,
        '9' => 9,
        'T' => 10,
        'J' => 1,
        'Q' => 12,
        'K' => 13,
        'A' => 14,
        _ => panic!()
    }
}

impl Hand {
    fn new(cards: &'static str, bid: i64) -> Hand {
        let mut complete_hand_type: &str = "HighCard";
        let mut hand_type_rank: i64 = 0;

        for joker_rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'] {
            let mut letter_map: HashMap<char, _> = HashMap::new();
            for char in cards.chars() {
                letter_map.entry(char).and_modify(|count| *count += 1).or_insert(1);
            }
            let joker_entry = letter_map.remove_entry(&'J');
            let target_character_entry = letter_map.entry(joker_rank);
            if let Some(joker_entry) = joker_entry {
                target_character_entry.and_modify(|count| *count += joker_entry.1).or_insert(joker_entry.1);
            }

            let mut hand_type: &str = "HighCard";
            let card_count: Vec<_> = letter_map.values().cloned().collect();
            for (outer_rank, outer_count) in letter_map.iter() {
                if *outer_count == 2 {
                    let mut largest_count = 0;
                    for (inner_rank, inner_count) in letter_map.iter() {
                        if outer_rank == inner_rank {continue;}
                        if *inner_count > largest_count {
                            largest_count = *inner_count;
                        }
                    }
                    if largest_count == 2 {
                        hand_type = "TwoPair"
                    } else {
                        hand_type = "OnePair"
                    }
                }
            }
            if card_count.contains(&3) {
                if card_count.contains(&2) {
                    hand_type = "FullHouse"
                } else {
                    hand_type = "ThreeOfAKind"
                }
            }
            if card_count.contains(&4) {
                hand_type = "FourOfAKind"
            }
            if card_count.contains(&5) {
                hand_type = "FiveOfAKind"
            }

            if hand_type_rank < get_hand_type_rank(hand_type) {
                hand_type_rank = get_hand_type_rank(hand_type);
                complete_hand_type = hand_type;
            }
        }

        Hand {
            cards,
            bid,
            hand_type: complete_hand_type,
        }
    }
}

fn main() {
    //let lines: Vec<&str> = include_str!("../test.txt").lines().collect();
    let lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();

    let mut hand_map: HashMap<i64, Vec<Hand>> = HashMap::new();

    for line in lines {
        let hand_info: Vec<&str> = line.split_whitespace().collect();
        let bid: i64 = hand_info[1].parse().unwrap();
        let hand: Hand = Hand::new(hand_info[0], bid);
        if let Some(entries) = hand_map.get_mut(&get_hand_type_rank(&hand.hand_type)) {
            entries.push(hand);
        } else {
            hand_map.insert(get_hand_type_rank(hand.hand_type), vec![hand]);
        }
    }

    for hand_type in hand_map.iter_mut() {
        hand_type.1.sort_by(|a, b| {
            let a_cards: Vec<char> = a.cards.chars().collect();
            let b_cards: Vec<char> = b.cards.chars().collect();
            for i in 0..5 {
                if get_card_value(a_cards[i]) < get_card_value(b_cards[i]) {
                    return std::cmp::Ordering::Less;
                } else if get_card_value(a_cards[i]) > get_card_value(b_cards[i]) {
                    return std::cmp::Ordering::Greater;
                }
            }
            panic!("Identical cards!?");

        });
    }

    let mut hand_vec: Vec<Hand> = Vec::new();
    for i in 0..7 {
        if let Some(hand) = hand_map.get(&i) {
            hand_vec.extend(hand);
        }
    }
    println!("{:?}", &hand_vec);

    let mut accumulator = 0;
    for i in 0..hand_vec.len() {
        accumulator += (i + 1) as i64 * hand_vec[i].bid;
    }
    println!("{}", accumulator);
}