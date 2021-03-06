# CA - Chapter 4


<!-- vim-markdown-toc GFM -->
* [Terms](#terms)
* [Review of Instruction Formats](#review-of-instruction-formats)
* [Data Path](#data-path)
	* [Register File](#register-file)
	* [ALU](#alu)
	* [Data Memory Unit](#data-memory-unit)
	* [Branching](#branching)
	* [Single Datapath](#single-datapath)
* [Simple Implementation](#simple-implementation)
	* [ALU Control](#alu-control)
	* [Control Unit](#control-unit)
	* [R-type Instruction Path](#r-type-instruction-path)
	* [Load Instruction Path](#load-instruction-path)
	* [Branch-On-Equal Instruction Path](#branch-on-equal-instruction-path)
* [Extending the Simple Implementation](#extending-the-simple-implementation)

<!-- vim-markdown-toc -->

## Terms

- Assert: signal should be high
- Deassert: signal should be low

## Review of Instruction Formats

- Instructions are 32 bits wide
- Three formats: R, I, J

![Instruction formats](https://i.imgur.com/Rjs0cDq.png)

- **Op** (6): 6-bit opcode
- **Rs**, Rt, Rd: 5-bit source and dest. register numbers
- **sa**: 5-bit shift amount used by shift instructions
- **funct**: 6-bit function field for r-type
- **immediate**: 16-bit constant or PC-relative offset
- **address**: 26-bit target address of jump instruction

## Data Path

- To exec instruction, fetch instruction from memory
- Need:
  - Instruction memory
  - PC
  - Adder (to get next address)

![Figure 4.5](https://i.imgur.com/oWsKTEp.png)
![Figure 4.6](https://i.imgur.com/5CcfP5n.png)

- The second image combines the elements from the first

### Register File

- Processor's registers are stored in __register file__
  - Contains entire register state, can read/write
- Need ALU to operate on values from register file
- For writing:
  - Four inputs:
    - Three register numbers (5 bits wide each (32 regs))
    - One for data (32-bit)
  - Two outputs:
    - Both for data (32-bit)
  - Controlled by write control signal

![Register File, figure 4.7a](https://i.imgur.com/tC6331B.png)

### ALU

- Takes two 32-bit inputs
- Produces 32-bit output
  - Also 1-bit signal if output = 0
    - Useful for branch condition comparisons

### Data Memory Unit

- Required for reading and writing data to memory
- Requires __sign-extend unit__
  - Sign-extends 16-bit offset field, found in load/store word instructions, into a 32-bit signed value
  - i.e. `4($t0)`
  - Also used when branching: need to compute target address relative to instruction address
- Has read/write control signals, address input, and input for data to be written

![Data memory and sign-extend unit, figure 4.8](https://i.imgur.com/A5GtSmf.png)

### Branching

- __Branch target address__: address specified in branch which becomes new PC if branch taken. Given by sum of offset field of instruction and address of instruction following the branch.
- Branch instruction details:
  - Base for branch address is address of instruction following the branch
    - PC + 4 is next instruction which is computed in instruction fetch
      - Easy to use for base in computing branch target addr
  - Offset field is shifted left 2 bits so that it is a word offset
    - Increases range of offset field by 4X
- Branch datapath requirements:
  1. Compute branch target address
    - Done via sign extension unit and adder
  2. Compare register contents
    - Done with register file to supply two register operands
    - Can also be done in ALU
      - If numbers equal, subtracting will result in 0 (ALU's special signal)

![Branching datapath, figure 4.9](https://i.imgur.com/Hf8bRuQ.png)

### Single Datapath

- Combine datapaths for:
  - Instruction fetch (figure 4.6)
  - R-type and memory instructions (figure 4.10)
  - Branches (figure 4.9)

![Single, combined datapath, figure 4.11](https://i.imgur.com/BPejbkd.png)

- Mux added to discern b/w sequential (PC+4) or branch target instructions addresses to be written to the PC

## Simple Implementation

- Includes:
  - lw
  - sw
  - bew
  - arithmetic-logical (add, sub, AND, OR)
  - slt

### ALU Control

- Four control inputs, six instructions
  - Generated by control unit
    - Inputs:
      - Function field of instruction
      - 2-bit control field (ALUOp)
        - Add (00), substract (01), defer to function field (10)

|ALU Control Lines|Function|
|-|-|
|0000|AND|
|0001|OR|
|0010|add|
|0110|sub|
|0111|slt|
|1100|NOR|

- Uses of ALU
  - Load/store: compute memory address by addition
  - R-type: AND, OR, sub, add, slt
  - beq: subtraction to compare

![ALUOp truth table, figure 4.12](https://i.imgur.com/d5bvIy3.png)

### Control Unit

- Takes inputs, generates write signal for each state element, mux, and ALU control
- Below is an image that shows all the necessary muxes and control lines

![Figure 4.15](https://i.imgur.com/LxCvMe6.png)

- The control unit can set every control signal except for PCSrc
	- Needs to AND signal from control unit (aka "Branch") with Zero signal from ALU
	- Effects shown below

![Figure 4.16](https://i.imgur.com/8ZGnHi7.png)

- Control signals set via opcode bits 31-26

![Opcode, figure 4.18](https://i.imgur.com/szCRsXh.png)

- Full data path shown below

![full data path, Figure 4.17](https://i.imgur.com/44Nt0Zl.png)

### R-type Instruction Path

![R-type datapath, figure 4.19](https://i.imgur.com/MzouXkD.png)

- Trace for `add $t1, $t2, $t3`:
	1. Instruction fetched, PC incremented
	1. Two registers, `$t2 and $t3`, are read from register file, control unit computes setting of control lines
	1. ALU operates on data read in from register file using function code to get ALU function
	1. Result from ALU written to register file using instruction to select destination register (`$t1`)

### Load Instruction Path

![Load datapath, figure 4.20](https://i.imgur.com/XpUzwWr.png)

- Example `lw $t1, offset $t2`
	1. Instruction fetched from instruction memory, PC incremented
	1. Register (`$t2`) value read from reg file
	1. ALU gets sum of value read from reg file and sign-extended, lower 16 bits of instruction (`offset`)
	1. Sum from ALU used as address for data memory
	1. Data from memory unit written to register file, destination  given by bits 20:16 (`$t1`)

### Branch-On-Equal Instruction Path

![beq path, figure 4.21](https://i.imgur.com/48hYNd3.png)

- Similar to r-type, but ALU output used to discern if PC uses PC + 4 or branch target addr for next instruction address
- Example `beq $t1, $t2, offset`
	1. Instruction fetched from instruction memory, PC incremented
	1. Two registers (`$t1 and $t2`) read from register file
	1. ALU subtracts data values from register file. PC + 4 added to sign-extended lower 16 bits of instruction (`offset`), shifted left by two; result is branch target address
	1. Zero result from ALU used to decide what gets stored into PC

---

- Combining the datapaths shown above, the control signal input (op code) and its outputs can be organized

![Simple implementation control function, figure 4.22](https://i.imgur.com/erT3CEv.png)


## Extending the Simple Implementation

- Jump instruction
	- Similar to branch, but target PC computed differently
		- Upper 4 bits of current PC + 4
		- 26-bit immediate
		- Bits 00

![Jump, figure 4.24](https://i.imgur.com/7nxLDzu.png)
