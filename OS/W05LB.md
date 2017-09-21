# OS - Process Synchronization

> 2017/09/21
>
> Lecture A was substituted with quiz

- Test on 10/03

---


<!-- vim-markdown-toc GFM -->
* [Sync Problems](#sync-problems)
	* [Bounded-Buffer Problem](#bounded-buffer-problem)
	* [Reader/Writers Problem](#readerwriters-problem)
* [- **verify**](#--verify)
	* [Dining-Philosophers Problem](#dining-philosophers-problem)
* [Semaphore Problems](#semaphore-problems)
* [Monitors](#monitors)
	* [Condition Variables](#condition-variables)

<!-- vim-markdown-toc -->

- insert semaphore here

## Sync Problems

- Bounded-buffer
- Reader/writer
- ...

### Bounded-Buffer Problem

- *n* buffer cells
- Semaphore **mutex** init'd to 1
    - mutex= "mutual exclusion"
- Semaphore **...** init'd to ...
- Semaphore **...** init'd to ...
- include code for producer/consumer

### Reader/Writers Problem

- Data set shared among number of processes
    - Readers: only read data set
    - Writers: can both write and read data set
- Problem
    - ALlow multiple readers to read at same time
    - Only one single writer can access data simultaneously
- Variations
    - No read kept waiting unless writer has permission to use shared
    - Once writer reader, perform write asap
    - Problem solved by kernel providing read/write locks
- Shared data
    - Data set
    - Semaphore **wrt** init to 1
    - Semaphore **mutex** init to 1
    - Integer **readcount** init to 0

---

- If wait(var) = 0 or 1, continue, decrease var by one
    - if less than 0, don't continue
    - **verify**
---

### Dining-Philosophers Problem

- Philos spend lives thinking and eating, not interacting with neighbors
- Occasiaonlly try to pick up 2 chopsticks to eat from bowl (1 at a time)
- 5 philos
    - Shared data
        - 1 bowl of rice (data set)
        - only 5 chopsticks, there will be a deadlock
        - Semaphore **chopstick[5]** ...
- Deadlock handling
    - Allow at most 4 philos to be sitting
    - Allow philo to pick up chopsticks only if both are available
    - Asymmetric solution: odd-number philo picks up first the left chopstick then right. Even-number philos picks up right then left

## Semaphore Problems

- Incorrect usage
    - signal(mutex) ... wait(mutex)
    - wait(mutex) ... wait(mutex)
    - Omit of wait(mutex) or signal(mutex) (or both)

## Monitors

- Abstration for proc sync
- Abstract data type
- ...

### Condition Variables


