.data

str1: .asciiz "\nEnter first integer n1: "
str2: .asciiz "Enter first integer n2: "
str3: .asciiz "The greatest common divisor of n1 and n2 is "
str4: .asciiz "\nGo again? (y/n) "

response: .space 20

.text

input_loop:

	### User Input ###

	la $a0, str1           # load str1 address into $a0
	li $v0, 4              # load I/O code for string output
	syscall                # output str1

	li $v0, 5              # load I/O code for integer input
	syscall                # input integer n1 into $v0
	add $a1, $v0, $zero    # store n1 in $a1

	la $a0, str2           # load str2 address into $a0
	li $v0, 4              # load I/O code for string output
	syscall                # output str2

	li $v0, 5              # load I/O code for integer input
	syscall                # input integer n2 into $v0
	add $a2, $v0, $zero    # store n2 in $a2

	### GCD ###
	
	jal gcd
	move $s0, $v0

	la $a0, str3           # load str3 address into $a0
	li $v0, 4              # load I/O code for string output
	syscall                # output str3
	li $v0, 1              # load I/O code for integer output
	add $a0, $s0, $zero    # $a0 = $s0; put gcd result in $a0 for output
	syscall                # output result from gcd
	
	### Go again ###
	
	la $a0, str4           # load str1 address into $a0
	li $v0, 4              # load I/O code for string output
	syscall                # output str1
	
	la $a0, response
	li $a1, 3
	li $v0, 8              # load I/O code for integer input
	syscall                # input go again decision into $v0
	
	lb  $t7, 0($a0)
	
	beq $t7, 'y', input_loop
	beq $t7, 'Y', input_loop
	j exit

gcd:
	# a1, a2 are the two ints
	# gcd returned in v0
	abs $t0, $a1
	abs $t1, $a2
loop:
	beq $t1, $0, done
	divu $t0, $t1
	move $t0, $t1
	mfhi $t1
	j loop
done:
	move $v0, $t0
	jr $ra

exit: