# Computer Architecture

> 2017/08/22
>
> Week 01, Lecture A

## Parallelism

### Classes in apps

- Data-level parallelism
	- Many data items that can be operated on at the same time
- Task-level parallelism
	- Tasks can operate independently and in parallel

### Classes in arch

...

## Flynn's Taxonomy

- Single instruction stream, single data stream (SISD)
	- Uniprocessor
	- Standard sequential computer + ILP
- Single instruction stream, multiple data streams (SIMD)
	- Same instruction executed by multiple processors using diff data streams
	- Single instruction memory and control processor
	- Multiple data proc and each proc has own data memory
- Multiple instruction streams, single data stream (MISD)
	- No commercial implementation
- Multiple instruction streams, multiple data streams (MIMD)
	- Task-level parallelism
	- Each processor fetches own instructions and operates on its own data

## Defining Computer Architecture

- Old view:
	- ISA design
	- decisions regarding registers, mem addressing, addr modes, etc.
- "Real" comp arch:
	- Specific reqs of target machine
	- Design to maximizes performance within constraints:
		- cost
		- power
		- availability
	- Includes ISA, microarch, hardware

## Instruction Set Architecture (ISA)

- Programmer-visible interface to hw
- Consists of:
	- Instructions and instruction formats
	- Data ttypes, encodings, and representations
	- Programmable storage: registers and memory
	- Memory addressing
	- Addressing modes: to address instructions and data
	- Handling exceptional conditions (like division by zero)