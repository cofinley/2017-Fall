# Computer Architecture - Chapter 1 Continued

> 2017/08/29
> 
> Week 2, Lecture B

## Amdahl's Law

- Improving some part of the computer and expecting a proportional speedup

$$\text{Execution time}_{new} = \text{Execution time}_{old} \times \left( (1 - {Fraction}_{enhanced}) + \frac{Fraction_{enhanced}}{Speedup_{enhanced}} \right)$$

$$Speedup_{overall} = \frac{\text{Execution time}_{old}}{\text{Execution time}_{new}} = \frac{1}{(1-Fraction_{enhanced})+\frac{Fraction_{enhanced}}{Speedup_{enhanced}}}$$

Example:

- Program runs in 100 seconds on computer, with multiply operation taking up 80 seconds
- How much improvement in multiply performance to get 4 times faster?
- Solution:
	- Suppose improvement by factor $s$ 
	- 25 sec (4 times faster) = 80 sec / $s$ + 20 sec
	- $s =80 / (25-20) = 80 / 5 = 16$
	- Improve multiplication speed by $s=16$ times
- 5 times faster?
	- 20 sec (5 times faster) = 80 sec / $s$ + 20 sec
	- $s = 80 / (20-20) = \infty \;\; \therefore$ Impossible to speedup by 5 times!

# Chapter 2 - Instructions

- MIPS Architecture
- Execution and Integer Unit (EIU)
	- 32-bit registers
		- Denoted by '$' prefix
	- Integer mul/div
		- 64 bit registers
	- ALU
		- Control unit
- Floating Point Unit (FPU)
	- Coprocessor 1
	- 32-bit floating-point registers
	- FP arithmetic
- Trap and Memory Unit (TMU)
	- Coprocessor 0
- Memory
	- Byte-addressible
	- 4 bytes per word
	- Up to $2^{32}$ bytes = $2^{30}$ words
	- In instruction, memory address of the operand fits into one of the 32-bit registers

## MIPS General-Purpose Registers

- 32 GPRs
	- Assembler uses dollar notation ($) to name registers
		- \$0 to \$31
	- All registers 32-bits in MIPS32
	- Register $0 is always 0, cannot be changed
- Conventions
	- \$4-\$7 used for arguments
		- \$a0-\$a3
	- \$8-\$15 are temp vars
		- \$t0-\$t7
	- \$16-\$23 are saved vars
		- \$s0-\$s7


