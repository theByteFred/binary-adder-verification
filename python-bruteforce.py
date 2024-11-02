from itertools import product 

# python script for testing 2-bit binary adder logic
# note that the runtime is exponential in the number of variables

# logic functions on zeros and ones (instead of True and False)
def AND(a,b): return 1 if a and b else 0
def OR (a,b): return 1 if a or  b else 0
def XOR(a,b): return 1 if a !=  b else 0

print("test all cases ...")

for a1,a0,b1,b0 in product([0,1],repeat=4):
    s0 = XOR(a0,b0) 
    c1 = AND(a0,b0)
    x1 = XOR(a1,b1) 
    y1 = AND(a1,b1)
    s1 = XOR(c1,x1) 
    z1 = AND(c1,x1) 
    s2 = XOR(y1,z1)
    A = a0 + 2*a1
    B = b0 + 2*b1
    S = s0 + 2*s1 + 4*s2
    print(f"A={A} B={B} S={S} a0={a0} a1={a1} b0={b0} b1={b1} s0={s0} s1={s1} s2={s2} c1={c1} x1={x1} y1={y1} z1={z1}")
    assert(A+B == S)

print("verified!")
