// a way to estimate π c/o https://www.youtube.com/watch?v=FQ1k_YpyG_A

class pi_2 {
    final static double pi_valid = 3.141592653589793238;
    final static long num_steps = (long)1e+9;
    final static double step = 1.0 / (double)num_steps;

    public static void main (String [] args) {
        double x, total;

        total = 0.0;
        for (long i = 0; i < num_steps; i ++) {
            // 0.5 for "midpoint Riemann sum"
            x = (i + 0.5) * step; 
            total += 4.0 / (1.0 + x * x);
        }
        double pi = step * total;

        System.out.printf ("%.16f %.16f\n", pi, pi_valid);
    }
}

