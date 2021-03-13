# CSCI 206 Computer Organization & Programming
# Date: 2011-09-13
# Revised 2019-10-31 for RISC-V
#
# Copyright (c) 2011 Bucknell University
#
# Permission is hereby granted, free of charge, to any individual or
# institution obtaining a copy of this software and associated
# documentation files (the "Software"), to use, copy, modify, and
# distribute without restriction, provided that this copyright and
# permission notice is maintained, intact, in all copies and
# supporting
# documentation.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL BUCKNELL UNIVERSITY BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
# Student name: Tung Tran
#
# data segment -------------------------------------
	.data	 
	.align 2
 
save:
	.word 0,0,0,0,7,0,0,0,0,0 	# array save[.]
ivar:
	.word 0 			# int i
kvar:
	.word 0 			# int k
donestring:
	.asciz "i= "
promptstring:
	.asciz "Enter the value to search for: "
valnotfoundstring:
	.asciz "value not found."
newline:
	.asciz "\n"
# code segment --------------------------------------
	.text
init:
	li a7, 4
	la a0, promptstring
	ecall
	li a7, 5
	ecall
	addi s6, a0, 0
	#li a7, 4
	#la a0, newline
	#ecall

	li 	s3, 0 		# store 0 in i
	la	t1, ivar
	sw 	s3, 0(t1)
	addi 	s5, zero, 10 		# store string length in k
	la	t1, kvar
	sw 	s5, 0(t1)
        la 	s4, save 	# put the address of save[0] in $s4
        add 	t0, zero, s6 	# t0=userinput
        
test:
	# reserve t1 for byte offset of save array
	add	t1, zero, s3 	# t1 = i
	beq 	t1, s5, notfound
	slli	t1, t1, 2 	# cnvert index to byte addres (multiply t1 by 4)
	add	t1, t1, s4	# t1 = &save[0] + t1 (byte address of save[i])
	lw	t2, 0(t1)	# t2 = save[i]
	beq	t2, t0, found
	addi	s3, s3, 1
	j	test
	
notfound:
	la a0, valnotfoundstring
	li a7, 4
	ecall
	j terminate
	 
found:
	la	a0, donestring
	li	a7, 4
	ecall
	
	add	a0, zero, s3		# print value of i
	li	a7, 1
	ecall
	    
terminate:
	li 	a7, 10 		# terminate program
	ecall	
	
