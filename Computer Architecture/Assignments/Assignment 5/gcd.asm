#***************************************************************************************************

# Connor Finley
# Computer Architecture
# HW 5 - GCD
# 2017/10/29

#***************************************************************************************************

.data

str1: .asciiz "\nEnter first integer n1: "
str2: .asciiz "Enter first integer n2: "
str3: .asciiz "The greatest common divisor of n1 and n2 is "
str4: .asciiz "\nGo again? (y/n) "

response: .space 20

.text

input_loop:

    # User Input

    la $a0, str1            # load str1 address
    li $v0, 4               # Use sysycallcode for string output
    syscall                 # output string

    li $v0, 5               # Input first integer into $t0
    syscall
    move $t0, $v0

    la $a0, str2            # Load second prompt same way as first
    li $v0, 4
    syscall

    li $v0, 5               # Input second integer into $t1
    syscall
    move $t1, $v0

    #***************************************************************************************************

    # Get GCD, print result
    
    jal gcd                 # Call GCD function and print result

    la $a0, str3            # Output result string
    li $v0, 4
    syscall

    li $v0, 1               # Output result integer (gcd)
    move $a0, $s0           # Load result for syscall
    syscall

    #***************************************************************************************************

    # Repeat prompt

    la $a0, str4            # Prompt user to go again
    li $v0, 4
    syscall
    
    la $a0, response        # Capture y/n response
    li $a1, 3
    li $v0, 8
    syscall
    
    lb  $t7, 0($a0)         # Determine result and repeat if necessary, else exit
    
    beq $t7, 'y', input_loop    # Check for case-insensitive 'y' answer
    beq $t7, 'Y', input_loop
    j exit

#***************************************************************************************************

# Calculate GCD

gcd:

    abs $t0, $t0            # Normalize a and b inputs with absolute value
    abs $t1, $t1

loop:

    beq $t1, $0, done       # Until b is 0, divide a by b
    divu $t0, $t1
    move $t0, $t1           # a <- b
    mfhi $t1                # b <- remainder
    j loop

done:

    move $s0, $t0           # Store result
    jr $ra                  # Go back to caller line

exit:

    li $v0, 10              # Exit program
    syscall