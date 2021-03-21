# CSCI 206 Computer Organization & Programming
# Date: 2011-09-19
# Revised: 2019-11-04 for RISC-V
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
#
# This program uses a procedure xfind to find a particular character.
# See detailed instructions in lab handout

.data
# Define constants here
strprompt: .asciz "Enter a string to search:"
charprompt: .asciz "Enter the character to search for:"

# allocate 100 bytes to store the string
string: .space 100

.text

main:
	la a0, strprompt
	li a7, 4			# print prompt string
	ecall

	la a0, string			# load address of string
	li a1, 100			# max input length
	li a7, 8 			# read string
	ecall

	la a0, charprompt
	li a7, 4			# print string
	ecall

	li a7, 12 			# read char
	ecall

	mv a1, a0			# move search char to a1
	la a0, string			# load addr of string into a0
	jal	xfind			# call xfind

# TODO
# write code here to print the result of the
# call to xfind
	li a7, 34			# Print addr in hex, a0 now holds addr
	ecall


	li	a7, 10			# exit to OS
	ecall

# write the code of function xfind after this label
xfind:

	# TODO search the string pointed to by a0 for the character in a1
	# if found, return the address of the first match
	# if not found, return 0 (NULL)
	
	lb t1, 0(a0)			# t1 = value of addr at a0
	beq t1, zero, return_null
	beq t1, a1, return_addr
	addi a0, a0, 1			# Addr of next index
	
	j xfind

return_addr:
	jr ra
	
return_null:	
	li a0, 0
	jr ra
