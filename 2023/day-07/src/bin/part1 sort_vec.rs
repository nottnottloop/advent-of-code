#![allow(warnings)]

use std::collections::HashMap;

#[derive(Debug, Copy, Clone)]
struct Hand {
    cards: &'static str,
    bid: i64,
    hand_type: &'static str,
    hand_type_rank: i64
}

impl Hand {
    fn new(cards: &'static str, bid: i64) -> Hand {
        let mut letter_map: HashMap<_, _> = HashMap::new();
        for char in cards.chars() {
            letter_map.entry(char).and_modify(|count| *count += 1).or_insert(1);
        }
        let mut letter_map: Vec<(_, _)> = letter_map.iter().collect();
        letter_map.sort_by(|a, b| b.1.partial_cmp(a.1).unwrap());
        println!("{:?}", letter_map);

        let mut hand_type: &str = "HighCard";
        let mut past_object: (&char, &i32) = (&'P', &-999);
        for letter_object in letter_map {
            if letter_object.1 == &5 {
                hand_type = "FiveOfAKind";
                break;
            }
            else if letter_object.1 == &4 {
                hand_type = "FourOfAKind";
                break;
            }
            else if letter_object.1 == &2 {
                if past_object.0 == &'P' { past_object = letter_object; continue; }
                else if past_object.1 == &3 {
                    hand_type = "FullHouse";
                    break;
                }
                else if past_object.1 == &2 {
                    hand_type = "TwoPair";
                    break;
                }
            }
            else if letter_object.1 == &1 {
                if past_object.0 == &'P' { past_object = letter_object; continue; }
                else if past_object.1 == &3 {
                    hand_type = "ThreeOfAKind";
                    break;
                }
                else if past_object.1 == &2 {
                    hand_type = "OnePair";
                    break;
                }
            }
            past_object = letter_object;
        }
        
        let hand_type_rank: i64 = match hand_type {
            "FiveOfAKind" => 6,
            "FourOfAKind" => 5,
            "FullHouse" => 4,
            "ThreeOfAKind" => 3,
            "TwoPair" => 2,
            "OnePair" => 1,
            "HighCard" => 0,
            _ => panic!()
        };

        //dbg!(letter_map);

        Hand {
            cards,
            bid,
            //hand_type,
            hand_type,
            hand_type_rank
        }
    }
}

fn main() {
    //let lines: Vec<&str> = include_str!("../inputs/example.txt").lines().collect();
    let lines: Vec<&str> = include_str!("../test.txt").lines().collect();

    let mut hand_map: HashMap<&str, Vec<Hand>> = HashMap::new();

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