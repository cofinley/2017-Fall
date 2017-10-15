# OS - Main Memory (cont'd)

> 2017/10/12

<!-- vim-markdown-toc GFM -->
* [Memory Protection](#memory-protection)
* [Shared Pages](#shared-pages)
* [Structure of Page Table](#structure-of-page-table)
	* [Hierarchical Page Tables](#hierarchical-page-tables)
	* [Two-level Page Table](#two-level-page-table)
	* [64-bit Logical Address Space](#64-bit-logical-address-space)
	* [Hashed Page Table](#hashed-page-table)
	* [Inverted Page Table](#inverted-page-table)
* [Segmentaion](#segmentaion)
	* [Segmentation Architecture](#segmentation-architecture)

<!-- vim-markdown-toc -->

## Memory Protection

- Done via associating protection bit with each frame to indicate if read-only or read-write allowed
- Valid-invalid bit attached to each entry in page table
	- Valid = assoc page is in the process' logical addr space, legal page
	- Invalid = page is not in process' logical addr space
	- Or use page-table-length-register (PTLR)
	- Valid/invalid bit sits next to frame number
- Any violations -> trap in kernel

## Shared Pages

- Shared code
	- One copy of read-only code shared among processes
	- Like threads sharing proc space
	- Useful for IPC
- Private code/data
	- Each proc keeps sep copy of code/data

## Structure of Page Table

- 32-bit logical addr space on computer
- Page size of 4 KB (2^12)
- Page table would have 1M entries (2^32/2^12)
- If each entry is 4 bytes -> 4 MB of physical addr space ...

### Hierarchical Page Tables

- Break up logical addr space into mul page tables
- ...

### Two-level Page Table

- ...

### 64-bit Logical Address Space

- Two-level not sufficient
- If page size is 4 KB
	- Page table has 2^52 entries
	- If two-level, ...
- ...

### Hashed Page Table

- Used when addr space > 32 bits
- Virtual page # hashed into page table
- Three parts
	1. Virtual page num
	2. Value of mapped page frame
	3. Pointer to next element
- ...

### Inverted Page Table

- Instead of having page table for each process, have a page table for all processes
	- One entry for each real page of memory
- Decreases memory needed to store each table
- Increases time needed to search table
- ...

## Segmentaion

> Know internal/external fragmentation, fixed/variable table size (?)

- Supports user view of memory
- Program is collection of segments
- Can be:
	- Main program
	- Procedure
	- Function
	- Method
	- Object
	- Variables
	- etc.

### Segmentation Architecture

- Logical addr = (segment-number, offset)
- Segment table: maps 2D physical addr
	- base: starting physical addr where segment resides in mem
	- limit: length of segment
- Segment table base reg
- Segment-table length reg
