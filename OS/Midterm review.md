# Midterm Review

<!-- TOC -->

- [OS](#os)
	- [OS structures](#os-structures)
- [Processes](#processes)
	- [States](#states)
	- [Creations](#creations)
	- [IPC](#ipc)
- [Threads](#threads)
	- [User/kernel Level](#userkernel-level)
	- [Multithreading models](#multithreading-models)
- [Processor Synchronization](#processor-synchronization)
	- [Peterson's solution](#petersons-solution)
	- [Semaphores](#semaphores)
	- [Bounded-buffer problem](#bounded-buffer-problem)
- [Scheduling](#scheduling)
	- [Criteria](#criteria)
	- [Algos](#algos)
		- [FCFS](#fcfs)
		- [SJF](#sjf)
		- [SRTF (Preemptive SJF)](#srtf-preemptive-sjf)
		- [Priority Scheduling](#priority-scheduling)
		- [Round Robin](#round-robin)
- [Scheduling in threading system](#scheduling-in-threading-system)
- [Algo evaluation](#algo-evaluation)

<!-- /TOC -->

- Terms
	- **Preempt**: forcibly pause/interrupt execution of task and resume at later time
		- Process is "preempted" when it is scheduled out of execution and waits for the next time slice to run in
			- Context switch happens
		- OS can interrupt/preempt one process in favor of another process
		- Non-preemptive: process can't be interrupted
			- Processes voluntarily give up CPU

## OS

- What is OS?
	- OS is a colllection of programs that control the hardware
	- Kernel: program that is running all the time
		- OS runs processes in low-privilege state and provides service calls that invoke the kernel in high 
			- Allows computer hw to run efficiently
- Client/server
- Dual-mode operation, timer
	- Protect OS from itself and processes from each other
	- Timer used to preclude long wait times

### OS structures

- Simple
	- Most functionality, least space
	- No modules
	- Single tasking, single memory space
- Unix
	- Two parts:
		- System programs
		- Kernel
- Layered
	- Levels/layers of OS
		- Top: UI
		- Bottom: hardware
		- Each layer only builds off lower layers, not upper
	- Advantages: abstraction and better debugging (assuming lower levels are working properly)
- Microkernel
	- Moves as much from kernel to user space
	- Easier to extend
	- More reliable, less bugs (e.g. secure) b/c less in general
	- Slow: constant communication b/w user and kernel space
- Modular
	- Loadable kernel modules
	- OOD
	- Core components all separate
		- Loaded by kernel as needed
	- Like layered, but more flexible
- Hybrid
	- Combine for best balance of performance, security, usability

## Processes

- Not same as program, program only part of process
	- Program = passive, process = active
- Four parts:
	- Text
	- Data
	- Stack
	- Heap

### States

- **New** state: process created
- **Running**: CPU being used by process
- **Blocked/Waiting**: I/O completion needed
- **Ready**: process ready, but waiting for other process
- **Terminated**: process finished execution
- Transitions
	- Transition one: process discovers it can't continue
		- Running -> Blocked
	- Transition 2: scheduler decides that running process has run long enough, let other process have a turn
		- Running -> Ready
	- Transition 3: all other processes have had their turn, time for first process to run again
		- Ready -> Running
	- Transition 4: external event occurs which allows process to continue
		- Blocked -> Ready
	- Transition 5: process created
		- New -> Ready
	- Transition 6: finished executing
		- Running -> Terminated

![Process States](https://www.studytonight.com/operating-system/images/process-state.png)

### Creations

- Look to quiz for these two
- Processes created with `fork()`
	- Use `wait()` to have parent wait for child to finish

### IPC

- Reasons
	- Information speedup
	- Performance speedup
	- Modularity
	- Convenience
- Shared-memory
	- Store/load from memory
		- Can be hard when syncing multiple processes
	- Good for large data
- Message-passing
	- Mailbox/port concept
		- Procs establish comm link (logical or physical)
	- Happens in kernel
		- Via system call, which can be slow
	- Good for small data
	- Easier to implement

## Threads

- Benefits of multithreading
	- Parallelism
	- Responsiveness (not all work blocked at one time)
	- Resource sharing
	- Economy
	- Scalability

### User/kernel Level

- User:
	- Threads only visible to process, only process visible to kernel
	- Good:
		- Can be implemented in OS with direct thread support
		- Doesn't mod OS
		- Simple mgmt.
		- Fast
	- Bad
		- No coop b/w OS
		- Requires multi-threaded kernel, otherwise major blocking
- Kernel:
	- Kernel sees all kernel-level threads
	- Good:
		- OS can prioritize the processes with more threads
		- Good for frequently blocking processes
	- Bad:
		- Slow
		- Big overhead to be able to block every thread
- Context switching
	- User level faster b/c uses library, kernel level uses syscall, so it's longer

### Multithreading models

- Many-to-one:
	- Many user threads to one kernel thread
	- One block -> all blocked
- One-to-one:
	- Each user thread has one kernel thread
	- More concurrency
	- Not great since each user thread requires slow startup of kernel thread
- Many-to-many:
	- Many user threads to one kernel thread
	- Only needs a sufficient amount of slower kernel threads
	- Better efficiency
- Two-level
	- Like M-M, but allows user thread to be bound to kernel-level

## Processor Synchronization

- Critical section problem
	- Critical section is section of code that should only be accessed by one process
		- Variables, data, etc. accessed
	- Each process has a critical section segment code
		- Changes and read/writes
		- If process in critical section, all other processes need to be locked out
	- Protocol needed to solve this problem of locking out
		- Each process must ask permission to enter critical section in **entry section**, followed by **exit section**, then **remainder section**

	```c
	do {
		// section entry
			// critical section
		// section exit
			// remainder section
	} while(true);
	```

- Requirements of solution to critical section
	1. Mutual exclusion
		- Only one process accessing particular critical section at a time
		- If a process is executing its critical section, no other cooperating processes can be executing in their critical sections
	1. Progress
		- Make sure some work is getting done
		- If no process is busy in its critical section and there are some processes that want to enter their critical section, then one must be picked to progress
	1. Bounded-waiting
		- Make sure every process gets a chance to enter its own critical section
		- Prevents **starvation**
		- Limit on the number of times other processes are allowed to enter their critical sections after a process has made request to enter its critical section and before that request is granted

### Peterson's solution

- Two-process solution to critical section problem
- Assume LOAD and STORE instructions are atomic (can't be interrupted)
- Two variables shared:
	- `int turn`
		- Indicates whose turn it is to enter critical section
	- `Boolean flag[2]`
		- Array used to indicate if process ready to enter critical section
		- flag[i] = true implies process i is ready

```c
do {
	flag[i] = true;
	turn = j;
	while (flag[j] && turn == j);

	//critical section

	flag[i] = false;

	//remainder section
} while (true);
```

### Semaphores

- Sync tool that is more sophisticated than mutex lock
- *S* variable
- Only accessed by `wait()` and `signal()`
	- Both atomic (can't be interrupted)
	```c
	wait(S) {
		while (S <= 0)
			; // busy wait, no operation
		S--;
	}

	signal(S) {
		S++;
	}
	```
	```c
	Semaphore mutex;  // init'd to 1
	do {
		wait(mutex);
		// critical section
		signal(mutex);
		// remainder section
	} while(true);
	```
	- Basically says the first process can go through into crit section (since `mutex` is > 0), but blocks subsequent processes from progressing into crit section (since `mutex` now <=0) until the first one finishes by calling `signal()` (when `mutex` is again > 0)
	- With **counting** semaphores, can have bigger range of cooperating processes
		- Can adjust max values to allow more processes in crit section at a time
	- With **binary** semaphores (true/false values), it can only lock and unlock (aka mutex lock) to show that a process is in crit section and others should wait
		- Can only have one process in crit section at a time

### Bounded-buffer problem

- *N* buffer cells
- Semaphore **mutex** init'd to 1
	- mutex = "mutual exclusion"
- Semaphore **full** init'd to 0
- Semaphore **empty** init'd to *N*

![Bounded-Buffer Problem](https://i.imgur.com/O7Xfi2t.png)

---

## Scheduling

> Know how to quickly calculate waiting and turnaround time

- Max CPU utililization done with multi-programming
- **CPU-I/O burst cycle**
	- Process execution consists of a cycle of CPU execution and I/O wait
- CPU burst followed by I/O burst
- I/O-bount has many short CPU bursts
- CPU-bound has few long bursts
- Distribution b/w the two is important
- **Non-preemptive scheduling**
	- Process removed from cpu by itself (syscall) or interrupt
		- After interrupt done, CPU can be assigned to any process that's waiting
- **Preemptive sheduling**:
	- OS/kernel can suspend a currently running process and switch to another based on scheduling algorithm
	- If interrupt causes removal of process from CPU, after interrupt done, CPU assigned back to that process

### Criteria

- CPU utilization
	- Want to maximize
- Throughput
	- Number of processes that complete their execution per time unit
	- Want to maximize
- Turn-around time
	- Amount of time to execute a process
	- Want to minimize
- Waiting time
	- Amount of time process waits in ready queue
	- Want to minimize
- Response time
	- Time it takes from when request submitted until first response produced (not output)
	- Want to minimize

### Algos

#### FCFS

- Non-preemptive
	- Processes assigned to CPU in same order as ready queue
- Easy to implement and fair
- Low overall throughput

![FCFS](https://i.imgur.com/vPjkupn.png)

---

![FCFS Convoy](https://i.imgur.com/24NqNAK.png)

#### SJF

- Assoc. process with length of its next CPU burst
	- Prioritize shorter burst times
- Non-preemptive
	- Once CPU given to the process it cannot be preempted until completes its CPU burst
	- The first process will always go first
		- After it finished, find shortest process that has already arrived to go next
- Gives min. waiting time (optimal)
	- Avg. wait time: sum of (start\_time - arrival\_time)_i / number\_of\_processes
- Non-preemptive not good for time-sharing
- Difficult to know length of next CPU request
- No discrimination?

#### SRTF (Preemptive SJF)

- After each interrupt, pick process with shortest next burst time
- Preemptive
	- If a new process arrives with CPU burst length less than remaining time of current executing process, preempt

![SRTF](https://www.studytonight.com/operating-system/images/sjf-preemptive.png)

- Image above says preemptive SJF, but is same thing as SRTF
	- P1 starts, but as soon as a shorter process comes, P1 is preempted
- Can produce min. avg. wait time
	- Avg. wait time: sum of (start_time1 - start_time2? - arrival_time) / number_of_processes
- Increased overhead

#### Priority Scheduling

- Priority number assoc with each process
- CPU alloc to highest priority number
- SJF is this where priority is inverse of predicted next burst time
- Problem with starvation
- Solution is **aging** – as time progresses increase the priority of the process

#### Round Robin

- Each process gets small unit of cpu time (**time quantum**)
	- After time elapsed, process is preempted and added to end of ready queue
- Timer interrupts every quantum to schedule next process
- Performance
	- q large => FIFO
	- q small => q must be large wrt context switch, else overhead is too high
- Easy to implement for time-sharing and fair
- Better response time
- Worse avg. turnaround time
- no discrimination

## Scheduling in threading system

- If threads supported, threads are scheduled, not processes
- Thread library schedules user-level threads on lightweight processes (LWP)
- Kenel-level threads scheduled on CPU compete with all threads in system

## Algo evaluation

- How to find best scheduling algo for an OS
- Deterministic modeling
	- Take predetermined workload and define performance of each algo on that workload
- Queueing modeling
	- Probabilistic
	- Usually exponential, described by mean
- Simulations
	- Accurate
	- Control simulated computer system (clock, data structures)
	- Data-driven
	- Gather stats
	- Still requires time/memory
- Implementation
	- Actually try the algos out
	- Most accurate
	- High risk/cost on real systems
	- Environments can vary