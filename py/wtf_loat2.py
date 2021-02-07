#!/usr/bin/env python3

# this is just sad

print("Hey Python, does (0.7 + 0.2) + 0.1 equal 0.7 + (0.2 + 0.1)?")
b = ((0.7 + 0.2) + 0.1) == (0.7 + (0.2 + 0.1))
print("Python says: ", b)
if not b:
    print("Womp womp womp")

