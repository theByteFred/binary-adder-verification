this repo provides three programs to verify the logic of a 2-bit binary adder and a fourth program to verify the logic of a k-bit binary adder.

1. simple bruteforce verification of 2-bit adder in C: 
run "gcc c-bruteforce.c && ./a.out"

2. simple bruteforce verification of 2-bit adder in python: 
run "python python-bruteforce.py"

3. SMT-based verification of 2-bit adder in python: 
make sure that z3-solver is installed (e.g. using pip) and 
run "python python-SMT.py"

4. SMT-based verification of k-bit adder in python: 
make sure that z3-solver is installed (e.g. using pip) and 
run "python python-SMT-k.py [number of bits]"

Note: while bruteforce verification time grows exponential in the number of variables (input bits) and is therefore not suited if the number of inputs gets larger, the SMT-based can easily handly larger setups as well.
