init	00000
input r0 00001 000
array a, r0 01100 0000	000//create array a of size r0
im r1, 0 01001 001 0000	//0 in r1
label loop: 10001 0001
input r2 00001 010
store a:r1, r2 01011 0000 001 010
addi r1,r1,1 01000 001 001 0001	#if numeric, insert 1 in code
>r1, r0	01101 001 000	#if, pc+1 else, pc+2
jump exit_loop 00111 0010
jump loop 00111 0001
label exit_loop: 10001 0010
im r2, 0 01001 010 0000
im r3, 0 01001 011 0000
label sum: 10001 0011
load r1, a:r2 01010 001 0000 010	
add r3, r3, r1 00011 011 011 001
addi r2, r2, 1 01000 010 010 0001
> r2, r0 01101 010 000
jump exit_sum 00111 0100
jump sum 00111 0011
label exit_sum: 10001 0100
output r3 00010 011
halt 11111