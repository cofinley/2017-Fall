/*
  Connor Finley
  Operating Systems
  Project 1
  Sep. 9, 2017
*/

#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

/* key number */
#define SHMKEY ((key_t) 1622)

typedef struct
{
  int value;
} shared_mem;

shared_mem *total;

void process1() {
  while (total->value < 100000) {
    total->value += 1;
  }
  printf("From process 1: total = %d\n", total->value);
  exit(0);
}

void process2() {
  while (total->value < 200000) {
    total->value += 1;
  }
  printf("From process 2: total = %d\n", total->value);
  exit(0);
}

void process3() {
  while (total->value < 300000) {
    total->value += 1;
  }
  printf("From process 3: total = %d\n", total->value);
  exit(0);
}

void process4() {
  while (total->value < 500000) {
    total->value += 1;
  }
  printf("From process 4: total = %d\n", total->value);
  exit(0);
}

void main() {

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

  total->value = 0;
  
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
  
  waitpid(pid1, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid1);
  waitpid(pid2, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid2);
  waitpid(pid3, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid3);
  waitpid(pid4, NULL, 0);
  printf("Child with ID: %d has just exited.\n", pid4);


  // Detach segment
  if (shmdt(total) == -1){
    perror("shmdt");
    exit(-1);
  }
  
  // Deallocate segment
  shmctl(shmid, IPC_RMID, NULL);
  
  printf("\nEnd of program.\n");
}
