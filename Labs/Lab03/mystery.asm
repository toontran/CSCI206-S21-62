
# CSCI 206 Computer Organization & Programming
# Date: 2019-10-26
# Copyright (c) 2019 Bucknell University
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


	.data
	
unused:	.word 0xDEADBEEF			
						
x:	.word 89				
						
	.text	
main:						# This tells the simulator
						# where start your program

	
	add		t0, zero, zero		# Initialize t0 to 0
	add		s2, zero, zero		# Initialize s2 to 0

loop:
	add		s2, s2, t0		# Increment s2 by t0 (1+2+3+..+10), should be 55 when done looping
	addi		t0, t0, 1		# Increment t0 by 1
	addi		t3, t0, -10		# If t0 <= 10, jump to "loop"
	blez		t3, loop		

	la		t2, x			# Load address of x into t2, then store value of s2 there
	sw		s2, 0(t2)		# effectively changes the value of 2nd word from 89 to 55
	
	add		a0, zero, s2		# Move result into a0 for return code
	li		a7, 93			# Code (93) for system call Exit2
	ecall					# Exit!
	ebreak					# Break if something went wrong (should not get here!)

