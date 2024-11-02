// C prog for testing 2-bit binary adder logic

// logic functions on zeros and ones (instead of true and false)
#include <assert.h>
#include <stdio.h>

int AND(int a,int b){ return a && b; }
int OR (int a,int b){ return a || b; }
int XOR(int a,int b){ return a != b; }

int main()
{
    for(int a1=0;a1<=1;a1++)
    for(int a0=0;a0<=1;a0++)
    for(int b1=0;b1<=1;b1++)
    for(int b0=0;b0<=1;b0++)
    {
        int s0 = XOR(a0,b0);
        int c1 = AND(a0,b0);
        int x1 = XOR(a1,b1);
        int y1 = AND(a1,b1);
        int s1 = XOR(c1,x1);
        int z1 = AND(c1,x1);
        int s2 = XOR(y1,z1);
        int A = a0 + 2*a1;
        int B = b0 + 2*b1;
        int S = s0 + 2*s1 + 4*s2;
        printf("A=%d B=%d a0=%d a1=%d b0=%d b1=%d -> s0=%d s1=%d s2=%d c1=%d x1=%d y1=%d z1=%d\n", 
            A,B,a0,a1,b0,b1,s0,s1,s2,c1,x1,y1,z1);
        assert(A+B == S);
    }
    printf("verified.\n");
    return 0;
}

