# python script for verifying 2-bit binary adder logic using the SMT solver z3 (checkout z3 website for more background and nice examples)

import z3 # install using "pip install z3-solver"

a0 = z3.Bool('a0') # note: one could also use BitVec instead Bools
a1 = z3.Bool('a1') # but for didactical reasons I decided not to use it here
b0 = z3.Bool('b0')
b1 = z3.Bool('b1')

s0 = z3.Xor(a0,b0) 
c1 = z3.And(a0,b0)
x1 = z3.Xor(a1,b1) 
y1 = z3.And(a1,b1)
s1 = z3.Xor(c1,x1) 
z1 = z3.And(c1,x1) 
s2 = z3.Xor(y1,z1)

# Note: when using BitVecs, this part this part gets obsolete. However, the code might be less transparent for people who are not familiary with SMT/z3
A = z3.If(a0,1,0) + z3.If(a1,2,0)
B = z3.If(b0,1,0) + z3.If(b1,2,0)
S = z3.If(s0,1,0) + z3.If(s1,2,0) + z3.If(s2,4,0)

# check validity by checking the satisfiability of the complement
solver = z3.Solver()
solver.add(A+B != S)  
print("test1: complement:",solver.check())
assert(solver.check() == z3.unsat)
print("verified!")

# check validity using universal quantifier 
# from a logical point, this check is equivalent to the one above
# however, this code gives an illustration of universal quantifiers
solver = z3.Solver()
solver.add(z3.ForAll([a0,a1,b0,b1],A+B == S)) 
print("test2: universal-quantified formula:",solver.check())
assert(solver.check() == z3.sat)
print("verified!")

"""
# Note: to verify a k-bit adder just continue in the same veign, e.g. with a "for"-loop
.
.
.
s0 = z3.Xor(a0,b0) 
c1 = z3.And(a0,b0)

x1 = z3.Xor(a1,b1) 
y1 = z3.And(a1,b1)
s1 = z3.Xor(c1,x1) 
z1 = z3.And(c1,x1) 
c2 = z3.Xor(y1,z1)

x2 = z3.Xor(a2,b2) 
y2 = z3.And(a2,b2)
s2 = z3.Xor(c2,x2) 
z2 = z3.And(c2,x2) 
c3 = z3.Xor(y2,z2)
.
.
.

sk = ck # final carry bit
"""


