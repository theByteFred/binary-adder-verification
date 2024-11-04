# python script for verifying k-bit binary adder logic using the SMT solver z3 (checkout z3 website for more background and nice examples)

import z3 # install using "pip install z3-solver"
from sys import argv

k = int(argv[1]) # first command line parameter specifies the number of bits

A = z3.BitVec('a',k+1)
B = z3.BitVec('b',k+1)
S = z3.BitVec('s',k+1)
C = z3.BitVec('c',k+1)
X = z3.BitVec('x',k)
Y = z3.BitVec('y',k)
Z = z3.BitVec('z',k)

a = {i:z3.Extract(i,i,A)==1 for i in range(k+1)}
b = {i:z3.Extract(i,i,B)==1 for i in range(k+1)}
s = {i:z3.Extract(i,i,S)==1 for i in range(k+1)}
c = {i:z3.Extract(i,i,C)==1 for i in range(k+1)}
x = {i:z3.Extract(i,i,X)==1 for i in range(k)}
y = {i:z3.Extract(i,i,Y)==1 for i in range(k)}
z = {i:z3.Extract(i,i,Z)==1 for i in range(k)}

solver = z3.Solver()
solver.add(z3.Not(a[k]))
solver.add(z3.Not(b[k])) 

solver.add(s[0] == z3.Xor(a[0],b[0])) 
solver.add(c[1] == z3.And(a[0],b[0]))

for i in range(1,k):
	solver.add(x[i]   == z3.Xor(a[i],b[i])) 
	solver.add(y[i]   == z3.And(a[i],b[i]))
	solver.add(s[i]   == z3.Xor(c[i],x[i])) 
	solver.add(z[i]   == z3.And(c[i],x[i])) 
	solver.add(c[i+1] == z3.Xor(y[i],z[i]))

solver.add(s[k] == c[k]) 

# check validity by checking the satisfiability of the complement
solver.add(A+B != S)

print("test1: complement:",solver.check())
assert(solver.check() == z3.unsat)
print("verified!")


