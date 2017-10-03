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

## Background

- Processes can execute concurrently
    - If data shared, need to maintain consistency

## Critical Section Problem

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

### Solution to Critical Section Problem

1. Mutual Exclusion
    - If a process is executing its critical section, no other cooperating processes can be executing in their critical sections
2. Progress
    - Make sure some work is getting done
    - If no process is busy in its critical section and there are some processes that want to enter their critical section, then one must be picked to progress
3. Bounded Waiting
    - Make sure every process gets a chance to enter its own critical section
    - Prevents **starvation**
    - Limit on the number of times other processes are allowed to enter their critical sections after a process has made request to enter its critical section and before that request is granted

### Handling Critical Sections in OS

- **Preemptive**: allows preemption (interrupting, to later resume) of process when running in kernel mode
- Non-preemptive - runs until it exits kernel mode, blocks, or voluntarily yields CPI
    - Basically free of race conditions in kernel mode

### Peterson's Solution

- Two-process solution
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

### Mutex Locks

- Protect critical section by `acquire()` a lock then `release()` the lock
    - Calls must be atomic
        - Usually done via hardware instructions
- Requires **busy waiting**
    - Lock therefore called a **spinlock**

```c
acquire() {
    while (!available)
        // busy wait
        available = false;
}

require() {
    available = true;
}
```

```c
do {
    acquire();
    // critical section
    release();
    //remainder section
} while(true);
```

## Semaphore

- Sync tool that is more sophisticated than mutex lock
- *S* variable
- Only accessed by `wait()` and `signal()`
    - Both atomic
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

### Semaphore Usage

- **Counting semaphore**: int value that can range over unrestriced domain
- **Binary semaphore**: int value ranging between 0 and 1
    - Same as mutex lock

### Semaphore Implementation

```c
Semaphore mutex;  // init'd to 1
do {
    wait(mutex);
    // critical section
    signal(mutex);
    // remainder section
} while(true);
```

- Must guarantee no two process can call wait() and signal() on the same semaphore at the same time

## Sync Problems

- Bounded-buffer
- Reader/writer
- ...

### Bounded-Buffer Problem

- *N* buffer cells
- Semaphore **mutex** init'd to 1
    - mutex = "mutual exclusion"
- Semaphore **full** init'd to 0
- Semaphore **empty** init'd to N

![Bounded-Buffer Problem](https://i.imgur.com/O7Xfi2t.png)

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
