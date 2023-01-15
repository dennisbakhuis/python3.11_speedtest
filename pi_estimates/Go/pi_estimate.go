package main

import (
	"fmt"
	"math/rand"
	"time"
)

const (
	N_POINTS = 10000000
	N_TRIES = 10
)

func estimate_pi(n_points int) float64 {
	var (
		x, y, rad_squared, pi float64
		within_circle int
		r *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))
	)

   	for i := 0; i < n_points; i++ {
		x, y = r.Float64(), r.Float64()

		rad_squared = x*x + y*y
		if rad_squared <= 1 {
			within_circle++
		}
	}

	pi = float64(within_circle) / float64(n_points) * 4
	return pi
}

func main() {
	var total_time float64

	for i := 0; i < N_TRIES; i++ {
		start := time.Now().UnixNano()
		estimate := estimate_pi(N_POINTS)
		end := time.Now().UnixNano()
		seconds := float64(end - start) / 1000000000.0
		total_time += seconds
		fmt.Printf("Pi is approximately %v, and took %0.5fs to calculate\n", estimate, seconds)
	}

	fmt.Printf("\nEach loop took on average %0.5f to calculate.\n", total_time / N_TRIES)
}
