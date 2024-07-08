#![allow(warnings)]

use std::collections::HashMap;

#[derive(Debug, Copy, Clone, PartialEq, Eq, Hash)]
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind
}

#[derive(Debug, Copy, Clone)]
struct Hand {
    cards: &'static str,
    bid: i64,
    hand_type: HandType,
}

impl Hand {
    fn new(cards: &'static str, bid: i64) -> Hand {
        let hand_type: HandType;

        Hand {
            cards,
            bid,
            //hand_type,
            hand_type: HandType::FiveOfAKind,
        }
    }
}

fn main() {
    let lines: Vec<&str> = include_str!("../inputs/example.txt").lines().collect();

    let mut hand_map: HashMap<HandType, Vec<Hand>> = HashMap::new();

    for line in lines {
        let hand_info: Vec<&str> = line.split_whitespace().collect();
        let bid: i64 = hand_info[1].parse().unwrap();
        let hand: Hand = Hand::new(hand_info[0], bid);
        if let Some(entries) = hand_map.get_mut(&hand.hand_type) {
            entries.push(hand);
        } else {
            hand_map.insert(hand.hand_type, vec![hand]);
        }
    }
    dbg!(hand_map);
}