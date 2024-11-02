this repo provides three programs to verify the logic of a 2-bit binary adder circuit.

1. simple bruteforce verification in C, 
run "gcc c-bruteforce.c && ./a.out"

2. simple bruteforce verification in python, 
run "python python-bruteforce.py"

3. SMT-based verification in python, 
make sure that z3-solver is installed (e.g. using pip) and run "python python-SMT.py"

Note: while bruteforce verification time grows exponential in the number of variables (input bits), 
the SMT-based can easily handly larger setups as well.
