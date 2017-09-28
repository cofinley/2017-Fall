# OS - CPU Scheduling (cont'd)

> 2017/09/28

<!-- vim-markdown-toc GFM -->
* [Thread Scheduling](#thread-scheduling)
	* [Pthread Scheduling](#pthread-scheduling)
* [Multiprocessor Scheduling](#multiprocessor-scheduling)
	* [Load-balancing](#load-balancing)
	* [Multithread Multicore](#multithread-multicore)
* [Real-time CPU Scheduling](#real-time-cpu-scheduling)
* [Priority-based Scheduling](#priority-based-scheduling)
* [Virtualization and Scheduling](#virtualization-and-scheduling)
* [Rate Monotonic Scheduling](#rate-monotonic-scheduling)
* [Earliest Deadline First Scheduling (EDF)](#earliest-deadline-first-scheduling-edf)
* [OS Examples](#os-examples)
	* [Linux Scheduling](#linux-scheduling)
	* [Windows](#windows)
* [Algorithm Evaluation](#algorithm-evaluation)
	* [Queueing Models](#queueing-models)
	* [Little's Formula](#littles-formula)
	* [Simulations](#simulations)
	* [Implementation](#implementation)
* [Midterm Review](#midterm-review)
	* [OS](#os)
	* [Processes](#processes)
	* [Threads](#threads)
	* [Proc Sync](#proc-sync)
	* [Scheduling](#scheduling)

<!-- vim-markdown-toc -->

## Thread Scheduling

...

### Pthread Scheduling

...

- join = wait

## Multiprocessor Scheduling

- **Homogeneous processors** within a multiprocessor
- **(A)symmetric multiprocessor**
	- Symmetric - each processor is self-scheduling (most common)
		- All processes in common ready queue, or each has own private queue of read processes
- **Processor affinity** - process has affinity for processor it's currently running on
	- Soft
		- ...
	- Hard
		- Guarantee it will stay and not migrate to other processors
	
### Load-balancing

- If symmetric, need max CPU util
- Load-balancing keeps work distributed
- Push migration
	- Periodic check on eac proc, push from overloaded to other
- Pull migration
	- ...
- Contradicts with affinity, need to find balance


### Multithread Multicore

- Single thread waits for compute and memory stall cycles
- Multi-thread, offset to always have compute cycles going in parallel

## Real-time CPU Scheduling

- **Soft** - no guarantee when critical process will be scheduling
- **Hard** - task must be serviced before deadline
- Latencies
	1. Interrupt - time from start of interrupt to start of route that services interrupt
	1. Dispatch - time for schedule to take current process off CPU and switch to another
		- Conflict phase:
			1. Preemption of any process running in kernel mode
			1. Release ...

## Priority-based Scheduling

- For real-time, scheduler has to support preemptive, priority-based scheduling
	- Only guarantees soft realtime
- For hard real-time, must also meet deadlines
- Processes has periodic characteristics that require CPU and intervals

## Virtualization and Scheduling

- Schedule mult guests onto CPU
- Each guest does its own scheduling

## Rate Monotonic Scheduling

- Priority = inverse of period
- ...
- Missed deadlines ...

## Earliest Deadline First Scheduling (EDF)

- Priority based on shorter deadline

## OS Examples

### Linux Scheduling

- Version 2.5 moved to constant order O(1) scheduling
- Preemptive, priority based

### Windows

- Priority-based, preemptive scheduling
- Dispatcher is scheduler
- Highest priority thread runs next

---

- QUIZ
	1. yes
	1. 80, 65, 60 (?), lowered 

## Algorithm Evaluation

- Find best scheduling algo for an OS
- Deterministic modeling
- Takes predetermined workload and defines performance of each algo on that workload
	- Calc min avg waiting time on each
	- ...

### Queueing Models

- One way to evaluate algo
- Describe probabilistically
	- Usually exponential, described by mean
	- ...
- ...

### Little's Formula

- One way to evaluate algo
- n = avg queue length
- W = avg wait time in queue
- lambda = avg arrival rate into queue
- Law: in steady state, procs leaving queue must equal procs arriving
	- n = lambda * W
- Example:
	- ...
	
### Simulations

- Another way to evaluate algo
- Queueing models are limited, simulations are more accurate
	- Does still require time/memory

### Implementation

- Yet another way to evaluate algo
- Just implement and see
- ...

---

- QUIZ
	1. PCS uses thread lib, SCS all threads in system scheduled by OS
		- Only kernel can asign threads to CPU
	1. Queuing model, little's formula, sim, implementation

---

## Midterm Review

### OS

- What is OS?
- Client/server
- Dual-mode operation, timer
	- Protect OS from itself and processes from each other
	- Timer used to preclude long wait times
- OS structures

### Processes

- States
- Creations
	- Look to quiz for these two
- IPC
	- Reasons
	- Shared-memory
	- Message-passing

### Threads

- Benefits of multithreading
- User/kernel level
	- Differences
	- Context switching (user level faster b/c uses library, kernel level uses syscall, so it's longer)
- Multithreading models
	- one-to-one, etc.

### Proc Sync

- Requirements of solution to critical section
	1. Mutual exclusion
	1. Progress, waiting (?)
	1. Bounded-waiting
- Peterson's solution
- Semaphores
- Bounded-buffer problem

### Scheduling

> Don't spend too much time on this, know how to quickly calculate waiting and turnaround time

- Criteria
- Algos
	- FCFS, SJF, SRTF, Priority, Round Robin
- Scheduling in threading system
- Algo evaluation
	- Deterministic modeling
	- Queueing modeling
	- Simulations
	- Implementation
