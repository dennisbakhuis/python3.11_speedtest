# Simple Monte Carlo Pi estimation calculation

using Random
using Dates
using Statistics

function estimation_pi(nMonteCarlo::Int64) :: Float64
    nInside = 0 :: Int64
    for i = 1:nMonteCarlo
        x = rand()
        y = rand()
        if x^2 + y^2 < 1
            nInside += 1
        end
    end
    return 4 * nInside / nMonteCarlo
end

function main()
    result_lst = Float64[]
    nMonteCarlo = 10000000
    for i = 1:10
        t0 = now()
        pi = estimation_pi(nMonteCarlo)
        t1 = now()
        elapsed = Dates.value(t1 - t0) /1000
        println("Pi is approximately $(pi) and took $(elapsed) seconds to calculate")
        push!(result_lst, elapsed)
    end
    println("Each loop took on average $(mean(result_lst)) seconds to calculate.")
end

main()

