# difference between first field of line and first field of previous line
BEGIN {
    last = 0
}
{
    cur = $1
    printf ("%d\n", cur - last)
    last = cur
}
END {
}

