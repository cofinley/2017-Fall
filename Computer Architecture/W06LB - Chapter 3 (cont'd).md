# Comp Arch - Chapter 3 (cont'd)

> 2017/09/28

<!-- vim-markdown-toc GFM -->
* [Integer Division](#integer-division)
	* [Efficient Sequential Division](#efficient-sequential-division)
	* [Signed](#signed)
		* [Examples](#examples)
* [Integer Multiplication in MIPS](#integer-multiplication-in-mips)
* [Integer Division in MIPS](#integer-division-in-mips)
* [Int to String Conversion](#int-to-string-conversion)

<!-- vim-markdown-toc -->

## Integer Division

### Efficient Sequential Division

- Use HI and LO regs
- Init HI = remainder, LO = dividend
- ...

### Signed

- Simplest: remember signs
- Convert dividend/divisor to positive
	- Get 2's complement if negative
- Do unsigned division
- Compute signs of quotient and remainder
	- Quotient sign = dividend sign XOR divisor sign
	- remainder sign = dividend sign
- Negate quotient and remainder if signs are negative
	- Get 2's complement to convert them to negative

#### Examples

- Pos dividend and pos divisor
	- 17 / 3 => quotient = 5 remainder = 2
- Pos dividend and neg divisor
	- 17 / -3 => quotient = -5 ...

## Integer Multiplication in MIPS

- Multiply instructions
	- `mult $s1, $s2` (signed)
	- `multu $s1, $s2` (unsigned)
- 32-bit mult => 64-bit product
- Separate pair of 32-bit regs
	- HI = high-order 32-bit of product
	- LO = low-order 32-bit of product
- Special mul instruction
	- `mul $s1, $s2, $s3`
		- `$s0 = $s1 * $s2`
	- Put low-order 32-bits into destination reg
	- HI/LO undefined

## Integer Division in MIPS

- `div $s1, $s2`
- `divu $s1, $s2` (unsigned)
- Produces quotient and remainder
	- HI = 32-bit remainder
	- LO = 32-bit quotient
- No overflow or divide-by-0 checking
	- If divisor 0, unpredictable result
- Use mfhi, mflo to get result
	- `mfhi Rd` (move from HI to Rd)
	- `mflo Rd` (move from LO to Rd)

## Int to String Conversion

- 32-bit int to string
- To store 123456 int
	```asm
	.data
		var1: .word 123456
	```
- Store as string (7 bytes, one extra byte for \0 null terminator)
- ...
