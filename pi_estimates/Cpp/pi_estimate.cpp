#include "cstdio"

#include <random>
#include <chrono>

#include "cmath"

float estimate_pi(unsigned int n_points,
                  std::uniform_real_distribution<float> &dist,
                  std::mt19937 &generator) {
  
  float x, y, radius_squared;
  unsigned int within_circle = 0;
  
  for (unsigned int i=0; i < n_points; i++) {
    x = pow(dist(generator),2);
    y = pow(dist(generator),2);
    
    within_circle += (x + y - 1) < 0;
  }
  
  return (float)within_circle/n_points * 4;
}

int main() {
  double avg_time = 0;
  unsigned long long N_POINTS = 10000000, N_REPEATS = 10;
  
  typedef std::ratio<1l, 1000000000000l> pico;
  typedef std::chrono::duration<long long, pico> picoseconds;
  // since this does not need to happen in the inner loop to be valid
  std::random_device rd;  // seed for rng 
  std::mt19937 generator(rd()); 
  std::uniform_real_distribution<float> dist(0.0, 1.0);
  
  for (int i=0; i < N_REPEATS; i++) {
    auto begin = std::chrono::high_resolution_clock::now();
    auto pi = estimate_pi(N_POINTS, dist, generator);
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<picoseconds>(end - begin);
    // one picosecond is only 1e-12 seconds - hence the scaling is different than for other examples
    avg_time += elapsed.count() * 1e-12;
    printf("Pi is approximately %g and took %.5f seconds to calculate.\n",
           pi, elapsed.count() * 1e-12);
  }
  printf("Test run was done with %.2e points.", double(N_POINTS));
  printf("\nEach loop took on average %.5f seconds to calculate.\n",
         avg_time / N_REPEATS);
  return 0;
}
