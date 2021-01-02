#include <stdio.h>
#include <math.h>

// for reference
const double pi_valid = 3.141592653589793238;

// a not-so-optimal way to estimate π
int main () {
    const double step = 1e-9;
    const double stepsq = step * step;

    double total = 0.0;

    double c_init = 0.0;
    double y_prev = sqrt(1.0 - c_init * c_init);
    double c_end = 0.5;
    // scanning along the x axis starting at origin
    for (double c = c_init + step; c < c_end; c += step) {
        // height (opp) of triangle from center to unit hyp and step base
        double y = sqrt(1.0 - c * c);
        // distance in y to previous height
        double dy = y - y_prev;
        // unit distance to previous point (step is constant x distance)
        total += sqrt (dy * dy + stepsq);
        y_prev = y;
    }
    // we traced from 0 to sin(π/6) (0.5) on the x axis
    double pi = total * 6.0;
    printf ("%.16f %.16f\n", pi, pi_valid);
    return 0;
}

