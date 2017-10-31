#***************************************************************************************************

# Connor Finley
# Computer Architecture
# HW 5 - Searching a String
# 2017/10/29

#***************************************************************************************************

.data

str1:           .asciiz "\nEnter a string of at most 100 characters: "
str2:           .asciiz "\nEnter a character: "
str4:           .asciiz "\nEnter a string of two characters: "
str3:           .asciiz "\nNumber of occurrences of "
equalsign:      .asciiz " = "
str5:           .asciiz "\nRepeat (y/n)? "

input_str:      .space 101
single_char:    .space 1
double_char:    .space 2
response:       .space 1

.text

main:

    #***************************************************************************************************

    # Prompt user for sentence

    la $a0, str1                # load prompt string
    li $v0, 4                   # load syscall code for outputting string
    syscall

    # Input sentence

    la $a0, input_str           # Input sentence
    li $a1, 100                 # Buffer of 100 chars
    li $v0, 8                   # Syscall code for inputting char
    syscall

    # Convert to lowercase

    move $s2, $a0               # Copy address to use for lowercase conversion
    move $s4, $s2               # Copy start of lowercase conversion address
    jal to_lower
    move $t0, $s4               # Use start of lowercase string address for first occurrence search
    move $s0, $s4               # Use start of lowercase string address for second occurrence search

    #***************************************************************************************************

    # Prompt user for single character

    la $a0, str2                # Same as before
    li $v0, 4
    syscall

    # Input char

    la $a0, single_char
    li $a1, 2                   # Buffer of two bytes this time
    li $v0, 8
    syscall

    # Convert to lowercase

    move $s2, $a0               # Copy address for lowercase conversion
    move $s4, $s2               # Copy start of lowercase conversion address
    jal to_lower
    move $t1, $s4               # Use start of lowercase string address for first occurrence search

    #***************************************************************************************************

    # Count occurrences of single char in sentence

    lb $t5, 0($t1)              # Get inputtted single char
    li $t2, 0                   # Char occurrence counter

    countChr:

        lb $t3, 0($t0)          # Load the first byte from sentence
        beqz $t3, end1          # LF, go to end1
        seq $t4, $t5, $t3       # Note if chars equal
        add $t0, $t0, 1
        add $t2, $t2, $t4       # Increment occurrence counter if chars equal
        j countChr
    
    end1:

        la $a0, str3            # Print out "number of occurrences" string
        li $v0, 4
        syscall

        la $a0, 0($t1)          # Print out single char
        li $v0, 4
        syscall

        la $a0, equalsign       # Print out equal sign
        li $v0, 4
        syscall

        li $v0, 1               # Print counter's result
        move $a0, $t2
        syscall

    #***************************************************************************************************

    # Prompt user for two-char string

    la $a0, str4                # Same as above
    li $v0, 4
    syscall

    # Input two-char string

    la $a0, double_char         # Input two-char string
    li $a1, 3
    li $v0, 8
    syscall

    # Convert to lowercase

    move $s2, $a0               # Copy address for lowercase conversion
    move $s4, $s2               # Copy start of lowercase conversion address
    jal to_lower
    move $t1, $s4               # Use start of lowercase string address for second occurrence search

    #***************************************************************************************************

    # Count occurrences of two-char string in sentence

    move $t0, $s0               # Retrieve original sentence address for second occurrence search
    lb $s0, 0($t1)              # Get first of two inputtted chars from address
    lb $s1, 1($t1)              # Get second of two inputtted chars from address

    li $t2, 0                   # Two-char occurrence counter
    li $t5, 0                   # Marker 1 (first char match bool)
    li $t6, 0                   # Marker 2 (second char match bool)

    count2Chr:

        lb $t3, 0($t0)          # Load the first byte from inputted sentence
        beqz $t3, end2          # LF, go to end2

        seq $t6, $s1, $t3       # Note if char #2 equal to current char
        and $t7, $t5, $t6       # AND the two markers
        add $t2, $t2, $t7       # Use AND result to increment the counter if two-char string match

        move $t5, $zero         # Reset both markers
        move $t6, $zero

        seq $t5, $s0, $t3       # Note if char #1 equal to current char
        add $t0, $t0, 1         # Go to next char
        j count2Chr

    end2:

        la $a0, str3            # Print out "number of occurrences" string
        li $v0, 4
        syscall

        la $a0, 0($t1)          # Print double-char string
        li $v0, 4
        syscall

        la $a0, equalsign       # Print out equal sign
        li $v0, 4
        syscall

        li $v0, 1               # Print counter's result
        move $a0, $t2
        syscall

    #***************************************************************************************************

    # Repeat prompt

    repeat:

        la $a0, str5            # Same string prompt method as before
        li $v0, 4
        syscall
        
        la $a0, response        # Capture y/n response
        li $a1, 2
        li $v0, 8
        syscall
        
        lb  $t7, 0($a0)
        
        beq $t7, 'y', main
        beq $t7, 'Y', main
        j exit


    exit:

        li $v0, 10              # Exit
        syscall

#***************************************************************************************************

# Lowercase conversion function

to_lower:

    lb $s3, 0($s2)              # $s2 is string addr saved beforehand
    beqz $s3, return            # LF, return back to caller
    blt  $s3, 97, convert       # If ASCII less than 'a', convert
    
    return_here:                # Come back from conversion
    
        addi $s2, $s2, 1        # Next char
        j to_lower

convert:

    addi $s3, $s3, 32           # Add 32 to ASCII code
    sb $s3, 0($s2)              # Overwrite current char
    j return_here

return:

    jr $ra                      # Return back to main function calling line