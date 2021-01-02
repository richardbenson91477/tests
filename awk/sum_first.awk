# sum first field 
BEGIN {
    sum = 0
}
{
    sum += $1
}
END {
    printf ("%d\n", sum);
}

