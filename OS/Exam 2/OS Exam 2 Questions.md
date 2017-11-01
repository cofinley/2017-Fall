# OS Exam 2 Review

<!-- TOC -->

- [Deadlocks (Chapter 7)](#deadlocks-chapter-7)
	- [Necessary conditions](#necessary-conditions)
	- [Resource-Allocation Graph](#resource-allocation-graph)
	- [Prevention](#prevention)
	- [Avoidance](#avoidance)
		- [Banker's](#bankers)
	- [Detection](#detection)
	- [Wait-for graph](#wait-for-graph)
	- [Recovery](#recovery)
- [Main memory (Chapter 8)](#main-memory-chapter-8)
	- [Address binding](#address-binding)
	- [Logical/physical space](#logicalphysical-space)
	- [Allocation](#allocation)
		- [Fragmentation](#fragmentation)
	- [Segmentation](#segmentation)
	- [Paging](#paging)
		- [Method of Implementation](#method-of-implementation)
		- [EAT](#eat)
		- [Memory protection in paging system](#memory-protection-in-paging-system)
		- [Page Table Structure](#page-table-structure)
		- [Segmentation](#segmentation-1)
		- [Fragmentation](#fragmentation-1)
		- [Advantages of paging and segmentation](#advantages-of-paging-and-segmentation)
- [Virtual Memory (Chapter 9)](#virtual-memory-chapter-9)
	- [Benefits](#benefits)
	- [Demand paging](#demand-paging)
	- [Steps to handle page fault](#steps-to-handle-page-fault)
	- [EAT](#eat-1)
	- [Copy-on-write](#copy-on-write)
	- [Page replacement methods](#page-replacement-methods)
	- [Second chance algo](#second-chance-algo)
	- [Allocations of frames](#allocations-of-frames)
	- [Alloc algos](#alloc-algos)
	- [Global vs. local replacement](#global-vs-local-replacement)
	- [Thrashing](#thrashing)
	- [Working set model](#working-set-model)
	- [Prepaging](#prepaging)
	- [Page size implications (on fragmentation, page table size, etc.)](#page-size-implications-on-fragmentation-page-table-size-etc)
	- [Program structure](#program-structure)

<!-- /TOC -->

## Deadlocks (Chapter 7)

### Necessary conditions

1. Mutex
    - At least one resource must be held in a non-sharable mode
    - Only one process at a time can use the resource
2. Hold and wait
    - A proc must be holding 1+ resources and waiting on more that are held up by other procs
3. No preemption
    - Resources can't be preempted
      - Must be voluntarily released by process holding it
4. Circular wait
    - Cycle is preset (P0->R0->P1->R1->P0)
    - Happens when only one instance of resource type

### Resource-Allocation Graph

- Processes (circles) and resources (squares) are vertices
- Edges show relationship
  - Request: P_i -> R_i
  - Assignment: R_i -> P_i
- Resources with multiple instances have dots representing the number of instances inside their squares
- If cycle, possible deadlock
  - If cycle and a resource type has a single instance and is requested by multiple, then deadlock occurs

### Prevention

- Just need to prevent one of the four necessary conditions from happening
- Mutex: Can't help
- Hold and Wait: guarantee that when proc requests a resource, it doesn't hold other resources
- No preemption: if proc requests resources but must wait for them, preempt its currently held resources
  - The held resources are added to list of resources being waited on
- Circular wait: enumerate resources, use resources in increasing order

### Avoidance

- Disadvantages of preventative methods include low device utilization and system throughput
- Use information ahead of time to determine if proc should wait to avoid deadlock
  - Information: max number of each resource type needed
    - Leads into banker's algorithm

#### Banker's

- Known:
  - Available resources (vector of length _m_)
  - Allocation: _n_ x _m_ matrix, defines # of resources of each type allocated to each proc to begin with
  - Max (requested): _n_ x _m_ matrix, defines total resource need for each resource type and each proc
- Unknown:
  - Need: _n_ x _m_ matrix, (Max - allocation)

### Detection

![Detection algorithm](https://i.imgur.com/y4AkURY.png)

### Wait-for graph

### Recovery

- Two methods:
  - Abort **all**
    - Big expense
  - Abort **one at a time** until deadlock cycle gone
    - Big overhead
    - Choose one victim, suspend its resources, rollback (restart) check again for deadlock
      - Victim factors:
        1. Priority
        2. Total computation time thus far
        3. How many/what kind of resources (simple to preempt?)
        4. How many resources left until complete
        5. How many procs will need termination
        6. Proc interactive or batch
      - If deadlock still, choose second victim
    - Disadvantage: starvation of processes
      - One process may be preempted every time
        - Solve by factoring in # of rollbacks

## Main memory (Chapter 8)

### Address binding

1. Compile time
    - If you know where the process will reside in memory
    - Absolute location code
    - Train ticket example (know exactly what cabin you have)
2. Load Time
    - If you don't know where the process will go
    - Relocatable code
    - Plane ticket example (don't know exact seat until boarding pass)
3. Execution time
    - If process is moved during execution
    - Bus ticket example (can move around en route)

### Logical/physical space

- Logical: address generated by CPU
  - AKA virtual address
  - Only type seen by user program
- Physical: address seen by memory unit
- Compile & load time binding generate the same logical and physical addresses
  - Execution time binding gives different addresses
    - Differing address __spaces__
- Mapping from virtual->physical taken care of by memory management unit (MMU)
- Use __dynamic loading__ for better memory space utilization
  - Like lazy loading, subroutines only loaded from disk when called
  - Good for large programs and when memory is small
  - __Dynamic linking__ is similar, but is done at execution time
    - Prevent libraries from having to be included in every program's binary that needs it
      - Dynamically linked libraries (DLLs)
    - __Stub__ (short library loading code block) used for each reference
    - Works well for version updates; any references will be automatically updated

### Allocation

- Protection
  - Don't want process to access memory it doesn't own
  - Include a limit register that its logical address must abide by
- Partitions
  - Fixed-size
    - One process for each
  - Variable size
    - Starts with one big hole of memory
      - Filled up by processes, left with various-sized holes
      - OS picks hole for process in input queue
        - Hole chosen with scheduling algorithm (best fit, worst fit, first fit)
          - __Dynamic storage allocation problem__
        - If hole too large, split in two
          - Merge contiguous holes

#### Fragmentation

- **External**
  - As processes come and go, free memory space is broken into small pieces
  - External fragmentation happens when enough total memory for request, but spaces not contiguous
  - Happens with first-fit and best-fit strategies
  - __50% rule__: with _N_ allocated blocks, another 0.5 _N_ blocks will be lost to fragmentation
  - Solution: __compaction__
    - Rearrange all free memory into one large block
    - Possible only if relocation is dynamic and done at execution time
      - Can just relocate and change base register
    - Not possible if relocation is static and done at assembly or load time
    - Can be expensive
  - Other solution: allow non-contiguous memory for process
    - Achieved through __segmentation__ or __paging__
- **Internal**
  - Fragmentation that's internal to a partition
  - Happens with fixed partitions when process doesn't use whole partition size

### Segmentation

- Maps programmer's view to actual physical memory
- A logical address space is a collection of segments
  - Segment has name, length, number, and offset
    - logical address: <segment-number, offset>
- Map 2D logical address to 1D physical address using __segment table__
  - Table is array of base-limit register pairs
  - Offset must not go beyond segment's limit

### Paging

- Like segmentation, this allows process' physical address space to be non-contiguous
  - Unlike segmentatin, paging avoids external fragmentation and need for compaction
    - Also solves problem of fitting various-sized memory chunks in backing store during swapping
      - Backing store has fragmentation problems and access is slow so compaction is impossible
    - Can have internal fragmentation
- Split physical memory into fixed-sized blocks called **frames**
- Split logical memory into same-sized blocks called __pages__
- Load process' pages into any available frames when ready to execute
- Backing store spit into fixed-sized blocks same size as frames for clusters of frames
- Advantage: logical space can be bigger than physical space
- Logical address: __page number (p)__ and __page offset (d)__
  - Page number used as index in __page table__
    - Page table contains base address of each page in physical memory
      - Combine with offset to define real address

![Page table](https://i.imgur.com/6yuid2f.png)

- __Frame table__ keeps track of all frames in memory
  - One entry for each physical page frame

#### Method of Implementation

- Registers
  - Good if page table small (~256 entries)
- Memory
  - Pointed to by __page-table base register (PTBR)__
    - Good if switching between multiple tables
    - Disadvantage is memory access time
      - Have to access memory twice:
        1. Need to first index the table (provides frame number)
        1. Then need to find byte (uses page offset, provides actual byte)
      - Solve with hardware cache: __translation look-aside buffer (TLB)__
        - Instant lookup
        - Needs to be kept small, thou

---

- TLB
  - Entry format: key/tag, value
  - Contains page-table entries
  - Logical address' page number presented to TLB
    - If found (_hit_), return frame number
    - If not found (_miss_), need to make memory reference to actual page table

![TLB](https://i.imgur.com/SKxPjwV.png)

#### EAT

- __Hit ratio__: % of times a given page number found in TLB
- __Effective memory-access time__: probablistic time to get page table lookup
  - (hit ratio %) * TLB access time + (1 - hit ratio %) * (TLB access time + Memory access time)
  - Example:
    - TLB hits 80% of the time
    - 100 ns time to access memory
    - 100 ns time for memory-mapped access in TLB lookup
    - If TLB miss, that means we've done a TLB lookup already (100 ns), but now need to also access the memory (page table, another 100 ns), totalling a 200 ns lookup
    - EAT = 0.8 * 100 ns + 0.2 * 200 ns = 120 ns

#### Memory protection in paging system

- Done via protection bits associated with each frame kept in page table
  - Bit can mean page is read-write or read-only
  - Checked as physical address is computed
  - Illegal op => hardware trap
- Valid-invalid bit
  - Attached to each page table entry
  - _Valid_: page is in process's logical address space and is therefore a legal page
  - _Invalid_: page not in logical space, illegal addresses trapped
  - Can result in internal fragmentation
    - If page extends half into valid space and half into invalid space, the invalid half of the page can't be used, but is still allocated
- Rarely is the address range fully used in a process
  - Use __page-table length register (PTLR)__ to indicate size of page table
    - Check every logical address to make sure addres is in valid range for process

#### Page Table Structure

- Hierachical (multilevel)
  - Large address space => big page table for each process
  - Split up page table twice (outer and inner)
    - Use two page numbers and an offset for the logical address
    ![Hierarchical Page Table](https://i.imgur.com/zbANrAW.png)
    ![Two-part address](https://i.imgur.com/riWxN2e.png)
- Inverted
  - Solves problem of huge page table and smaller physical memory
  - Page table has only one page for each frame
    - Entry contains virtual address of page stored in real memory location __and__ process information (i.e. pid)
    ![Inverted page table](https://i.imgur.com/cgyrDSd.png)
  - Only one page table in the system
- Disadvantages
  - Inverted
    - Increase search time of page table
      - Lookup on virtual address but sorted by physical address  
      - Use hash table to help
    - Harder to implement shared memory
      - Shared memory has multiple virtual addresses (one for each process) pointing to same physical address
        - Can't do when one-to-one mapping in inverted scheme

#### Segmentation

- Protection

#### Fragmentation

#### Advantages of paging and segmentation

- Sharing/protection easier in segmentation system

## Virtual Memory (Chapter 9)

- Memory management topics in chapter 8 usually required the entire process to be in memory before execution
  - Limits size of program to size of physical memory
  - Often, entire program not needed in memory
- Virtual memory is a technique that allows execution of process not completely in memory
  - Separation of logical memory from physical memory
    - Allows for very large virtual memory
- Not easy to implement

### Benefits

- Allows programs to be larger than physical memory, easy sharing/shared memory, efficient process creation
- Program not constrained by limit of physical memory
- Less physical memory being used means more simultaneous programs in memory
- Less I/O needed to swap => faster programs

### Demand paging

- AKA lazy swapping
- Load pages only as needed during program execution
  - Fast timing
- Program on disk swapped into memory with __pager__
  - Only swaps in what's needed page-by-page
- Need valid-invalid bit to tell between pages in memory vs. disk
  - Valid: page valid and in memory
  - Invalid: page either not valid or valid but on disk
    - Access attempt -> page fault

![Demand Paging](https://i.imgur.com/VMbcIFy.png)

- In picture above, the cylinder is the disk
  - Pages A-H are on the disk, but only those that are needed (A,C,F) are loaded into the page table and marked with the valid bit

---

> __Note:__ pages are said to be on 'disk', but this is technically 'secondary memory'. This is usually a section of a disk known as the __swap space__. This happens when setting up linux and a swap partition is made. On windows, the page file is located on the disk with a `.swp` extension which also holds pages of RAM.

### Steps to handle page fault

- Page faults happen when trying to access page with invalid bit

![Steps](https://i.imgur.com/9ji1AOv.png)
![Steps verbose](https://i.imgur.com/OgHEYjN.png)

### EAT

- If no page faults, EAT = memory access time
- If page fault, read page from disk and access desired word
- EAT = (1-p) * memory access time + p * page fault time
- Need to know time needed to service fault
  - Procedures involved include:
    - Service page-fault interrupt
    - Read in page
    - Restart process

### Copy-on-write

- Child process involved

### Page replacement methods

- Problem: multiprogramming runs multiple processes and each process allocates N pages, but may only use N/2 of them
  - __Over-allocation__
  - If page fault, then get page from disk. But if not enough memory to place page, then we need to swap/replaces pages in memory to make room.
- If no frame free, find one that's not currently being used and free it
  - Free a __victim__ frame by writing contents to swap space and remove from page/frame tables
  - Read in desired page into newly freed frame, update page/frame tables
  - Continue from where fault occured
  - Doubles page fault service time (swap out _and_ in)
    - Reduce overhead with __modify bit__ in page/frame table entry

---

- FIFO Page Replacement
  - When page fault, replace page which is oldest in page frame
  ![FIFO](https://i.imgur.com/0fhpBch.png)
- Optimal
  - Replace page which won't be used for the longest period of time
  - Guarantees lowest possible page fault rate for fixed number of frames
  ![Optimal](https://i.imgur.com/8e8Br87.png)
- Least Recently Used (LRU)
  - Replace page that has not been used for longest period of time
  ![LRU](https://i.imgur.com/tCHAm7R.png)

### Second chance algo


### Allocations of frames


### Alloc algos


### Global vs. local replacement

- Global: choose victim from any process
- Local: choose victim that's making new reference in a specific process (helps with thrashing)

### Thrashing


### Working set model


### Prepaging


### Page size implications (on fragmentation, page table size, etc.)

### Program structure

