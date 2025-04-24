fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut safe_reports = 0;
    for line in lines {
        let nums: Vec<_> = line
            .split_whitespace()
            .map(|c| c.parse::<i32>().unwrap())
            .collect();
        let mut safe_report = false;
        
        for element_to_remove in 0..nums.len() {
            let mut this_iteration_safe = true;
            let mut new_nums = nums.clone();
            new_nums.remove(element_to_remove);
            println!("{:?}", new_nums);
            let mut windows = new_nums.windows(2).peekable();
            let mut decreasing: bool = true;
            if let Some(pair) = windows.peek() {
                if pair[0] < pair[1] {
                    decreasing = false;
                } else {
                    decreasing = true;
                }
            }

            while let Some(pair) = windows.next() {
                let this_window_decreasing: bool;
                if pair[0] < pair[1] {
                    this_window_decreasing = false;
                } else {
                    this_window_decreasing = true;
                }
                if decreasing != this_window_decreasing || pair[0] == pair[1] {
                    this_iteration_safe = false;
                    break;
                }
                if pair[0].abs_diff(pair[1]) > 3 {
                    this_iteration_safe = false;
                    break;
                }
            }
            if this_iteration_safe {
                safe_reports += 1;
                break;
            }
        }


        //if safe_report {
        //    safe_reports += 1;
        //}
    }
    println!("Safe reports: {:?}", safe_reports);
}
