#!/bin/bash

function x {
    while [ -n "$1" ]; do
        X=$(expr $X \* $1)
        shift
    done
}

X=1
x $(seq 1 10)

echo $X

