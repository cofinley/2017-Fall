---
title: "Computer Architecture - HW 2"
author: "Connor Finley"
date: "September 21, 2017"
output: pdf_document
---

## 1

> Bits have no inherent meaning. Given the 32-bit pattern:
> `1010 1101 0001 0000 0000 0000 0000 0010`
> What does it represent, assuming it is …

### a)

> A 2's complement signed integer?

Negative binary; flip the bits and add one:
`1010 1101 0001 0000 0000 0000 0000 0010`
`0101 0010 1110 1111 1111 1111 1111 1101`
`0101 0010 1110 1111 1111 1111 1111 1110`
=-1,391,460,35022222222

### b)

> A MIPS instruction?

- Op code (first 6 bits): `1010 11`
  - Not 0, so not R-type instruction
  - Equal to `0x2B` => store word instruction (`sw`)
- `sw rt imm(rs)`
  - Format: `0x2B rs rt imm`
  - 5-bit`rs=01 000` = 8, $8, or $t0 (source)
  - 5-bit`rt=1 0000` = 16, $16, or $s0 (destination)
  - 16-bit`imm=0000 0000 0000 0010`  = 2
- `sw $16 2($8)` or `sw $s0 2($t0)`
- Means that `MEM[$8+2] = $16` or `MEM[$t0+2] = $s0`

## 2

> Determine the absolute value of a signed integer. Show the implementation of the following pseudo-instruction using three real instructions:
>
> `abs $t1, $t2`

```asm
sra $t1,$t2,31
xor $t2,$t2,$t1
subu $t1,$t2,$t1
```

## 3

> For each pseudo-instruction in the following table, produce a minimal sequence of actual MIPS instructions to accomplish the same thing. You may use the `$at` for some of the sequences. In the following table, `imm32` refers to a 32-bit constant.

### a

> `move $t1, $t2`

```asm
addu $t1, $zero, $t2
```

### b

> `clear $t5`

```asm
and $t5, $t5, $zero
```

### c

> `li $t5, imm32`

```asm
addiu $t5, $zero, imm32
```

### d

> `addi $t5, $t3, imm32`

```asm
addi $t0, $zero, 0xFFFF		# create mask
andi $t1, $t0, imm32		# get bottom bits using mask
xori $t2, $t1, imm32		# get top bits by filtering out bottom bits
or $t5, $t1, $t2		# combine into t5
add $t5, $t3, $t5		# add $t3
```

### e

> `beq $t5, imm32, Label`

### f

> `ble $t5, $t3, Label`

### g

> `bgt $t5, $t3, Label`

### h

> `bge $t5, $t3, Label`