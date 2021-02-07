BEGIN {
    for (n = 0.0; n <= 1.0; n += 0.1)
        printf ("%.16f\n", n)

    if (n != 1.0)
        printf ("failed\n")

    exit
}

