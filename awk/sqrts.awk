BEGIN {
    for (n = 1.0; n < 4.0; n += 0.1)
        printf ("%.16f\n", sqrt(n))
    exit
}

