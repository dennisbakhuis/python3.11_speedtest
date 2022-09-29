use rand;
use std::time::Instant;

const N_POINTS: i32 = 10000000;
const N_REPEATS: i32 = 10;

fn estimate_pi(n_points: i32) -> f64 {
    let mut radius_squared: f64;
    let mut within_circle = 0;
    for _ in 0..n_points {
        let x: f64 = rand::random();
        let y: f64 = rand::random();
        radius_squared = x * x + y * y;
        if radius_squared <= 1f64 {
            within_circle += 1;
        }
    }
    (within_circle as f64 / n_points as f64 * 4f64) as f64
}
fn main() {
    let mut avg_time: f64 = 0.0;
    for _ in 0..N_REPEATS {
        let start = Instant::now();
        let pi = estimate_pi(N_POINTS);
        let duration = start.elapsed();
        avg_time += duration.as_secs_f64();
        println!(
            "Pi is approximately {} and took {} seconds to calculate",
            pi,
            duration.as_secs_f64()
        )
    }
    println!(
        "Each loop took average {} seconds to calculate.",
        avg_time / N_REPEATS as f64
    )
}
