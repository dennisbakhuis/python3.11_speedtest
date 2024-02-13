use std::time::Instant;
use rand::Rng;

fn main() {
    // Main function to execute the Monte Carlo Pi estimation multiple times and calculate the average time taken.
    let mut result_lst = Vec::new();  // Initialize a vector to store the time taken for each calculation
    let n_monte_carlo = 10_000_000;   // Number of random points to be used in each Pi estimation

    for _ in 0..10 {
        let start = Instant::now();          // Record the start time
        let pi = estimation_pi(n_monte_carlo); // Estimate Pi using the Monte Carlo method
        let elapsed = start.elapsed();        // Calculate the time taken for the current iteration

        // Print the estimated Pi value and the time taken for the current iteration
        println!("Pi is approximately {} and took {:?} to calculate", pi, elapsed);
        
        result_lst.push(elapsed);  // Store the elapsed time in the result list
    }

    // Calculate and print the average time taken for the Pi estimations
    let average: f64 = result_lst.iter().map(|d| d.as_secs_f64()).sum::<f64>() / result_lst.len() as f64;
    println!("Each loop took on average {} seconds to calculate.", average);
}

fn estimation_pi(points: usize) -> f64 {
    let mut rng = rand::thread_rng();
    let mut inside_circle = 0;

    for _ in 0..points {
        let x: f64 = rng.gen();
        let y: f64 = rng.gen();
        if x * x + y * y <= 1.0 {
            inside_circle += 1;
        }
    }

    4.0 * (inside_circle as f64) / (points as f64)
}
