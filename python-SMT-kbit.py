# python script for verifying 2-bit binary adder logic using the SMT solver z3 (checkout z3 website for more background and nice examples)

import z3 # install using "pip install z3-solver"
from sys import argv

k = int(argv[1]) # first command line parameter specifies the number of bits

a = {i:z3.Bool(f'a{i}') for i in range(k)} # first input
b = {i:z3.Bool(f'b{i}') for i in range(k)} # second input

s = {} # output
c = {} # internal auxiliary 1 ("carry")
x = {} # internal auxiliary 2
y = {} # internal auxiliary 3
z = {} # internal auxiliary 4

s[0] = z3.Xor(a[0],b[0]) 
c[1] = z3.And(a[0],b[0])

for i in range(1,k):
	x[i]   = z3.Xor(a[i],b[i]) 
	y[i]   = z3.And(a[i],b[i])
	s[i]   = z3.Xor(c[i],x[i]) 
	z[i]   = z3.And(c[i],x[i]) 
	c[i+1] = z3.Xor(y[i],z[i])

s[k] = c[k]

# Note: when using BitVecs, this part this part gets obsolete. However, the code might be less transparent for people who are not familiary with SMT/z3
A = sum(z3.If(a[i],2**i,0) for i in range(k))
B = sum(z3.If(b[i],2**i,0) for i in range(k))
S = sum(z3.If(s[i],2**i,0) for i in range(k+1))

# check validity by checking the satisfiability of the complement
solver = z3.Solver()
solver.add(A+B != S)  
print("test1: complement:",solver.check())
assert(solver.check() == z3.unsat)
print("verified!")

