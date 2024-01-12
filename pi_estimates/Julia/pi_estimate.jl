# Simple Monte Carlo Pi estimation calculation
using Random
using Statistics

function estimation_pi(nMonteCarlo::Int)
    # Estimates the value of Pi using the Monte Carlo method by simulating random points in a unit square
    # and calculating the ratio of points that fall inside the unit circle.

    nInside = 0
    for i in 1:nMonteCarlo
        x, y = rand(), rand()  # Generate random x and y coordinates between 0 and 1
        if x^2 + y^2 <= 1      # Check if the point (x, y) is inside the unit circle
            nInside += 1       # Count points inside the circle
        end
    end
    return 4 * nInside / nMonteCarlo  # Approximate Pi as 4 times the ratio of points inside the circle
end

function main()
    # Main function to execute the Monte Carlo Pi estimation multiple times and calculate the average time taken.

    result_lst = Float64[]  # Initialize an array to store the time taken for each calculation
    nMonteCarlo = 10000000  # Number of random points to be used in each Pi estimation

    for i in 1:10
        t0 = time()             # Record the start time
        pi = estimation_pi(nMonteCarlo)  # Estimate Pi using the Monte Carlo method
        t1 = time()             # Record the end time
        elapsed = t1 - t0       # Calculate the time taken for the current iteration

        # Print the estimated Pi value and the time taken for the current iteration
        println("Pi is approximately $(pi) and took $(elapsed) seconds to calculate")
        
        push!(result_lst, elapsed)  # Store the elapsed time in the result list
    end

    # Calculate and print the average time taken for the Pi estimations
    println("Each loop took on average $(mean(result_lst)) seconds to calculate.")
end

main()
