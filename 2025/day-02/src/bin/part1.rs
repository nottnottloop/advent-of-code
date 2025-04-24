fn main() {
    let mut lines: Vec<&str> = include_str!("../inputs/input.txt").lines().collect();
    let mut safe_reports = 0;
    for line in lines {
        let nums: Vec<_> = line
            .split_whitespace()
            .map(|c| c.parse::<i32>().unwrap())
            .collect();
        println!("{:?}", nums);
        let mut windows = nums.windows(2).peekable();
        let mut safe_report = true;
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
                safe_report = false;
                break;
            }
            if pair[0].abs_diff(pair[1]) > 3 {
                safe_report = false;
                break;
            }
        }
        if safe_report {
            println!("{:?}", line);
            safe_reports += 1;
        }
    }
    println!("{:?}", safe_reports);
}
