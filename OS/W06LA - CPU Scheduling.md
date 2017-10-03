# OS - CPU Scheduling

> 2017/09/26

<!-- vim-markdown-toc GFM -->
* [Basic Concepts](#basic-concepts)
* [CPU Scheduler](#cpu-scheduler)
* [Dispatcher](#dispatcher)
* [Scheduling Criteria](#scheduling-criteria)
* [Scheduling Algos](#scheduling-algos)
* [FCFS](#fcfs)
* [SJF](#sjf)
	* [Determine Length of CPU Burst](#determine-length-of-cpu-burst)
* [SRTF](#srtf)
* [Priority Scheduling](#priority-scheduling)
* [Round Robin](#round-robin)
* [Multilevel Queue](#multilevel-queue)
	* [Feedback Queue](#feedback-queue)

<!-- vim-markdown-toc -->

## Basic Concepts

- Max CPU utililization done with multi-programming
- **CPU-I/O burst cycle**
	- Process execution consists of a cycle of CPU execution and I/O wait
- CPU burst followed by I/O burst
- I/O-bount has many short CPU bursts
- CPU-bound has few long bursts
- Distribution b/w the two is important

## CPU Scheduler

- Scheduler selects from processes in ready queue, allocates cpu to one of them
- Scheduling decisions happen when process:
	1. Switches from running to waiting state (nonpreemptive)
	1. Switches from running to ready state
	1. Switches from waiting to ready
	1. Terminates
- **Non-preemptive scheduling**
	- Process removed from cpu by itself (syscall) or interrupt
		- After interrupt done, CPU can be assigned to any process that's waiting
- **Preemptive sheduling**:
	- If interrupt causes removal of process from CPU, after interrupt done, CPU assigned back to that process

## Dispatcher

- Gives control of CPU to process selected by short-term scheduler
	- Switch context
	- Switch to user mode
	- Jump to proper location in user program to restart program
- Dispatch latency
	- Time taken for dispatcher to stop one process and start another

## Scheduling Criteria

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

## Scheduling Algos

- First-come, first serve
- Shortest-job-first
- Shortest-remaining-time-first
- Priority
- Round robin

## FCFS

- Non-preemptive
	- Processes assigned to CPU in same order as ready queue
- Easy to implement and fair
- Low overall throughput

![FCFS](https://i.imgur.com/vPjkupn.png)

![FCFS Convoy](https://i.imgur.com/24NqNAK.png)

## SJF

- Assoc. process with length of its next CPU burst
	- Prioritize shorter burst times
- Non-preemptive
	- Once CPU given to the process it cannot be preempted until completes its CPU burst
- Gives min. waiting time (optimal)
- Non-preemptive not good for time-sharing
- Difficult to know length of next CPU request
- No discrimination?

> Looks like first process always goes first, confirm.

### Determine Length of CPU Burst

- Uses length of previous burst, using exponential averaging
1. $t_n$ = actual length of nth cpu burst
1. $\tau_{n+1}$ = predicted val for next burst
1. $\alpha,-0 \le \alpha \le 1$
1. Define: $\tau_{n=1} = \alpha t_n + (1-\alpha)\tau_n$

## SRTF

- After each interrupt, pick process with shortest next burst time
- Preemptive
	- If a new process arrives with CPU burst length less than remaining time of current executing process, preempt
- Can produce min. avg. wait time
- Increased overhead

## Priority Scheduling

- Priority number assoc with each process
- CPU alloc to highest priority number
- SJF is this where priority is inverse of predicted next burst time
- Problem with starvation
- Solution is **aging** – as time progresses increase the priority of the process

## Round Robin

- Each process gets small unit of cpu time (**time quantum**)
	- After time elapsed, process is preempted and added to end of ready queue
- Timer interrupts every quantum to schedule next process
- Performance
	- q large => FIFO
	- q small => q must be large wrt context switch, else overhead is too high
- ...
- Easy to implement for time-sharing and fair
- Better response time
- Worse avg. turnaround time
- no discrimination

## Multilevel Queue

- Ready queue partitioned into queus
	- Foregoround (interactive)
		- RR
	- Background (batch)
		- ...
- ...

### Feedback Queue

- Proc can move b/w queues, aging can be done this way
- Defined by:
	- no. of queues
	- sched. algos for each queue
	- Method used to know when to upgrade proc
	- Method used to ...

---

- QUIZ 1
- QUIZ 2
	- a.
		- q = 1
		- OH = 0.1
		- (10 / (10+1)) * 100 = 91%
	- b.
		- 20 / (10*1.1 + 10.1) * 100
