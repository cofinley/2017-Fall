/*
    Connor Finley (U50846049)
    Operating Systems
    Project 3 - Protected Bounded Buffer
    2017/10/28
*/


#define _REENTRANT
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <semaphore.h>

#define CAPACITY 15
#define SHMKEY ((key_t) 1622)


/***** Semaphores *****/


sem_t mutex;
sem_t empty;
sem_t full;


/***** Shared Memory Queue *****/


typedef struct
{
  char items[CAPACITY];
  int maxSize;
  int front;
  int rear;
  int size;
} queue;

queue *shared_q;


void q_enqueue(queue *q, char data);
char q_dequeue(queue *q);
void display(queue *q);


/**** Circular Queue Functions ****/


int isEmpty(queue *q) {
    return q->front == -1;
}

int isFull(queue *q) {
    return q->size == q->maxSize;
}

void q_enqueue(queue *q, char data) {
    if (!isFull(q)){
        if (q->front == -1) {
            // Initialize queue by setting front to something usable
            q->front = 0;
        }
        q->rear = (q->rear + 1) % q->maxSize;
        q->items[q->rear] = data;
        q->size++;
    }
}

char q_dequeue(queue *q) {
    if (!isEmpty(q)) {
        char item = q->items[q->front];
        if (q->front == q->rear) {
            // Once all items consumed, set indexes back to -1
            q->front = -1;
            q->rear = -1;
        }
        else {
            q->front = (q->front + 1) % q->maxSize;
        }
        q->size--;
        return item;
    }
}


/***** Threads *****/


void *producerThread (void *arg){
    char newChar;
    // Read file
    FILE* fp;
    fp= fopen("mytest.dat", "r");
    int doBreak = 0;
    while(1) {

        // Wait to produce until empty signal
        sem_wait(&empty);

        // Until full, keep producing
        while (!isFull(shared_q)) {

            // produce item in buffer
            int result = fscanf(fp, "%c", &newChar);

            if (result == -1) {
                // Replace EOF with asterisk so consumer knows when to stop
                newChar = '*';
            }
            
            sem_wait(&mutex);
            
            // add item to buffer
            q_enqueue(shared_q, newChar);

            sem_post(&mutex);

            if (result == -1) {
                // If EOF, break
                doBreak = 1;
                break;
            }
        }

        // Buffer full, signal to consumer
        sem_post(&full);
        // If EOF seen, break out of all loops
        if (doBreak) break;
    }

    close(fp);

    // Terminate thread
    pthread_exit(NULL);
} 

void *consumerThread (void *arg){
    int doBreak = 0;

     while(1){

        // Wait until full to start consuming
        sem_wait(&full);

        // Consume until empty
        while (!isEmpty(shared_q)) {

            sem_wait(&mutex);

            // remove item from buffer to buffer
            char nextChar = q_dequeue(shared_q);

            sem_post(&mutex);

            // Premature empty signal
            // Buffer not really empty, but a spot has opened up and producer
            //  can keep max buffer utilization by adding more until done.
            sem_post(&empty);

            // consume next item in buffer
            if (nextChar == '*'){
                // EOF, break out
                doBreak = 1;
                printf("\n");
                break;
            }
            else {
                // Print all non-EOF characters one-by-one on a single line
                fflush(stdout);
                printf("%c", nextChar);
            }

            // Wait 1 second
            sleep(1);
        }
        
        // If EOF seen, break out of all loops
        if (doBreak) break;
    }

    // Terminate thread
    pthread_exit(NULL);
}


void main() {

    int shmid;
    char *shmadd;
    shmadd = (char *) 0;

    // Create/allocate shared memory segment
    if ((shmid = shmget(SHMKEY, sizeof(queue), IPC_CREAT | 0666)) < 0)
    {
        perror("shmget");
        exit(1);
    }

    // Attach segment to address space
    if ((shared_q = (queue *) shmat(shmid, shmadd, 0)) == (queue *) -1)
    {
        perror("shmat");
        exit(0);
    }

    // Initialize queue
    shared_q->maxSize = CAPACITY;
    shared_q->size = 0;
    shared_q->front = -1;
    shared_q->rear = -1;

    // Initialize semaphores with correct values
    sem_init(&mutex, 1, 1);
    sem_init(&full, 1, 0);
    sem_init(&empty, 1, CAPACITY);

    // Create process id for producer thread
    pthread_t tidP[1];
    // Create process id for consumer thread
    pthread_t tidC[1];
    // Create attribute pointer array
    pthread_attr_t attr[1];
    fflush(stdout);

    // Required to schedule thread independently
    pthread_attr_init(&attr[0]);
    pthread_attr_setscope(&attr[0], PTHREAD_SCOPE_SYSTEM);  
    // end to schedule thread independently

    /* Create the threads */
    pthread_create(&tidP[0], &attr[0], producerThread, NULL);
    pthread_create(&tidC[0], &attr[0], consumerThread, NULL);
    
    // Wait for the threads to finish
    pthread_join(tidP[0], NULL);
    pthread_join(tidC[0], NULL);

    // Remove semaphores
    sem_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    // Detach shared memory segments
    if (shmdt(shared_q) == -1){
      perror("shmdt");
      exit(-1);
    }

    // Deallocate shared memory segments
    shmctl(shmid, IPC_RMID, NULL);    

    printf("\nEnd of program.\n");
}