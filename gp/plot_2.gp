default(realprecision, 32)

c(x) = [sin(x), cos(x)];

main() = {
    for(x=1, Pi * 200,
        cx = c(x / 100);
        print(cx[1], " ", cx[2]);
    );
    quit();
}

main();
