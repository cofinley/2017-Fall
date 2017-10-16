/*
  Connor Finley
  Operating Systems
  Project 2
  Oct. 10, 2017
*/

#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/sem.h>


/***** Shared Memory *****/

// Key number for `total` shared memory segment
#define SHMKEY ((key_t) 1622)

typedef struct
{
  int value;
} shared_mem;

shared_mem *total;


/***** Semaphores *****/

// Semaphore key
#define SEMKEY ((key_t) 505L)

// Define number of semaphores being created
#define NSEMS 1

// Create semaphore id
int sem_id;

// Semaphore buffers
static struct sembuf OP = {0, -1, 0};  // -1 is decrementing the semaphore value (wait)
static struct sembuf OV = {0, 1, 0};   // 1 is incrementing the sempahore value (signal) 
struct sembuf *P = &OP;
struct sembuf *V = &OV;

// Semapore union used to generate semaphore
typedef union{
  int val;
  struct semid_ds *buf;
  ushort *array;
} semunion;

// wait() semaphore operation
int POP()
{
  int status;
  status = semop(sem_id, P, 1);
  return status;
}

// signal() semaphore operation
int VOP()
{
  int status;
  status = semop(sem_id, V, 1);
  return status;
}


/***** Processes *****/


void process1() {
  
  // For each process, perform wait before handling critical section (`total->value` manipulation)
  POP();
  int i;
  for (i = 1; i <= 100000; i++) {
    total->value += 1;
  }
  // As soon as critical section done, call signal() before remainder section
  //  to trigger other processes
  VOP();

  printf("From process 1: total = %d\n", total->value);
  exit(0);
}

void process2() {
  
  POP();
  int j;
  for (j = 1; j <= 200000; j++) {
    total->value += 1;
  }
  VOP();

  printf("From process 2: total = %d\n", total->value);
  exit(0);
}

void process3() {
  
  POP();
  int k;
  for (k = 1; k <= 300000; k++) {
    total->value += 1;
  }
  VOP();

  printf("From process 3: total = %d\n", total->value);
  exit(0);
}

void process4() {
  
  POP();
  int l;
  for (l = 1; l <= 500000; l++) {
    total->value += 1;
  }
  VOP();

  printf("From process 4: total = %d\n", total->value);
  exit(0);
}

void main() {

  // Create process and shared memory vars
  int shmid, pid1, pid2, pid3, pid4, ID, status;
  char *shmadd;
  shmadd = (char *) 0;

  // Create/allocate shared memory segment
  if ((shmid = shmget(SHMKEY, sizeof(int), IPC_CREAT | 0666)) < 0)
  {
    perror("shmget");
    exit(1);
  }
  
  // Attach segment to address space
  if ((total = (shared_mem *) shmat(shmid, shmadd, 0)) == (shared_mem *) -1)
  {
    perror("shmat");
    exit(0);
  }

  // Initialize total
  total->value = 0;


  // Semaphore vars
  int value, value1;
  semunion semctl_arg;
  semctl_arg.val = 1;
  int semnum = 0;

  /* Create semaphores */
  sem_id = semget(SEMKEY, NSEMS, IPC_CREAT | 0666);
  if(sem_id < 0) printf("Error in creating the semaphore./n");

  /* Initialize semaphore */
  value1 = semctl(sem_id, semnum, SETVAL, semctl_arg);
  value = semctl(sem_id, semnum, GETVAL, semctl_arg);
  if (value < 1) {
    printf("Eror detected in SETVAL.\n");
  }
  
  // Fork four processes
  if ((pid1 = fork()) == 0) {
    process1();
  }
  
  if ((pid2 = fork()) == 0) {
    process2();
  }
  
  if ((pid3 = fork()) == 0) {
    process3();
  }
  
  if ((pid4 = fork()) == 0) {
    process4();
  }
  
  // Wait for all children to finish
  waitpid(pid1, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid1);
  waitpid(pid2, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid2);
  waitpid(pid3, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid3);
  waitpid(pid4, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid4);

  // Detach segments
  if (shmdt(total) == -1){
    perror("shmdt");
    exit(-1);
  }
  
  // Deallocate segments
  shmctl(shmid, IPC_RMID, NULL);

  // Deallocate semaphore
  semctl_arg.val = 0;
  status = semctl(sem_id, 0, IPC_RMID, semctl_arg);
  if( status < 0) {
    printf("Error in removing the semaphore.\n");
  }
  
  printf("\nEnd of program.\n");
}
