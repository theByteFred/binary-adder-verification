# python script for verifying 2-bit binary adder logic using the SMT solver z3 (checkout z3 website for more background and nice examples)

import z3 # install using "pip install z3-solver"

a0 = z3.Bool('a0') # note: one could also use z3.BitVec here
a1 = z3.Bool('a1') 
b0 = z3.Bool('b0')
b1 = z3.Bool('b1')

s0 = z3.Xor(a0,b0) 
c1 = z3.And(a0,b0)
x1 = z3.Xor(a1,b1) 
y1 = z3.And(a1,b1)
s1 = z3.Xor(c1,x1) 
z1 = z3.And(c1,x1) 
s2 = z3.Xor(y1,z1)

# note: when using BitVecs, this representation part is obsolete 
A = z3.If(a0,1,0) + z3.If(a1,2,0)
B = z3.If(b0,1,0) + z3.If(b1,2,0)
S = z3.If(s0,1,0) + z3.If(s1,2,0) + z3.If(s2,4,0)

# check validity by checking the satisfiability of the complement
solver = z3.Solver()
solver.add(A+B != S)  
print("test1: complement:",solver.check())
assert(solver.check() == z3.unsat)
print("verified!")
