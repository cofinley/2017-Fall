# OS - CPU Scheduling

> 2017/09/26

<!-- vim-markdown-toc GFM -->
* [Basic Concepts](#basic-concepts)
* [- Distribution b/w the two is important](#--distribution-bw-the-two-is-important)
* [CPU Scheduler](#cpu-scheduler)
* [Dispatcher](#dispatcher)
* [Scheduling Criteria](#scheduling-criteria)
* [Scheduling Algos](#scheduling-algos)
* [FCFS](#fcfs)
* [SJF](#sjf)
	* [Determine Length of CPU Burst](#determine-length-of-cpu-burst)
	* [Priority Scheduling](#priority-scheduling)
	* [Round Robin](#round-robin)
	* [Multilevel Queue](#multilevel-queue)
		* [Feedback Queue](#feedback-queue)

<!-- vim-markdown-toc -->

## Basic Concepts

- Max cpu util done w/ multi-programming
- CPU I/O burst cycle...
- ...
- I/O-bount has many short CPU bursts
- CPU-bound has few long bursts
- Distribution b/w the two is important
-

## CPU Scheduler

- Scheduler selects from processes in ready queue, allocates cpu to one of them
- Scheduling decisions happen when process:
	1. Switches ... (nonpreemptive)
		- Non-preemptive scheduling: process removed from cpu by ...
	1. ...

## Dispatcher

- Gives control of CPU to process selected by short-term scheduler
	- Switch context
	- Switch to user mode
	- Jump to proper location in user program to restart program
- Dispatch latency
	- Time taken for dispatcher to stop one process and start another

## Scheduling Criteria

- Maximize CPU util
- Max throughput
- ...

## Scheduling Algos

- First-come, first serve
- Shortest-job-first
- Shortest-remaining-time-first
- Priority
- Round robin

## FCFS

- Non-preemptive
- Easy to implement and fair
- Low overall throughput

## SJF

- Assoc. process with length of its next CPU burst
	- Prioritize shorter burst times
- Non-preemptive
- Gives min. waiting time
- Non-preemptive not good for time-sharing
- Difficult to know length of next CPU request
- No discrimination?

> Looks like first process always goes first, confirm.

### Determine Length of CPU Burst

- Uses length of previous burst, using exponential averaging
1. $t_n$ = actual length of nth cpu burst
1. $\tau_{n+1} = predicted val for next burst
1. $\alpha,-0 \le \alpha \le 1$
1. Define: $\tau_{n=1} = \alpha t_n + (1-\alpha)\tau_n$

### Priority Scheduling

- Priority number assoc with each process
- CPU alloc to highest priority number
- SJF is this where priority is inverse of predicted next burst time
- Problem with starvation
- ...

### Round Robin

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

### Multilevel Queue

- Ready queue partitioned into queus
	- Foregoround (interactive)
		- RR
	- Background (batch)
		- ...
- ...

#### Feedback Queue

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
