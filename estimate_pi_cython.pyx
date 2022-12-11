cdef extern from "stdlib.h":
    double drand48()
    void srand48(long int seedval)



def estimate_pi(
    n_points: int,
    show_estimate: bool,
) -> None:
    """
    Simple Monte Carlo Pi estimation calculation.

    Parameters
    ----------
    n_points
        number of random numbers used to for estimation.
    show_estimate
        if True, will show the estimation of Pi, otherwise
        will not output anything.
    """
    cdef float radius_squared
    cdef double x,y
    cdef int within_circle

    within_circle = 0

    for _ in range(n_points):
        # cdef float x = rand() / float(INT_MAX)
        # cdef float y = rand() / float(INT_MAX)

        x = drand48()
        y = drand48()
        radius_squared = x**2 + y**2

        if radius_squared <= 1:
            within_circle += 1

    pi_estimate = 4 * within_circle / n_points

    if not show_estimate:
        print("Final Estimation of Pi=", pi_estimate)
