BEGIN {
    x = 0
}
{
    x ++
    if (! (x % 2)) {
        printf ("%s %s\n", last, $0)
    }
    else {
        last = $0
    } 
}
END {
    exit
}

