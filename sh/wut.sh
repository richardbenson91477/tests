#!/bin/bash
# also works with mksh

python3 <<< "x = 10; print(x)"
<<<"print('hi')" python3

python << end
x = 10
print(x)
end

