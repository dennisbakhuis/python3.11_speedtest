#include <stdlib.h>
#include <stdio.h>
#include <chrono>
#include <array>

#define N_POINTS 10000000
#define N_REPEATS 5

float estimate_pi(int n_points) {
   double x, y, radius_squared, pi;
   int within_circle=0;

   for (int i=0; i < n_points; i++) {
      x = (double)rand() / RAND_MAX;
      y = (double)rand() / RAND_MAX;

      radius_squared = x*x + y*y;
      if (radius_squared <= 1) within_circle++;
   }

   pi=(double)within_circle/N_POINTS * 4;
   return pi;
}

int main() {
    double avg_time = 0;

    srand(42);

    for (int i=0; i < N_REPEATS; i++) {
        auto begin = std::chrono::high_resolution_clock::now();
        double pi = estimate_pi(N_POINTS);
        auto end = std::chrono::high_resolution_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
        avg_time += elapsed.count() * 1e-9;
        printf("Pi is approximately %g and took %.5f seconds to calculate.\n", pi, elapsed.count() * 1e-9);
    }

    printf("\nEach loop took on average %.5f seconds to calculate.\n", avg_time / N_REPEATS);
}

