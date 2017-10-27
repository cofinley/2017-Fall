#define _REENTRANT
#include <pthread.h>
#include <stdio.h>
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




typedef struct
{
  char items[15];
  int maxSize;
  int front;
  int rear;
  int size;
} queue;

queue *shared_q;


void q_enqueue(queue *q, char data);
char q_dequeue(queue *q);
void display(queue *q);


/***** Threads *****/

void *producerThread (void *arg){
    char newChar;
    FILE* fp;
    fp= fopen("mytest.dat", "r");
    int doBreak = 0;
    while(1) {

        // printf("waiting on empty...\n");
        sem_wait(&empty);
        

        while (!isFull(shared_q)) {
            int result = fscanf(fp, "%c", &newChar);

            if (result == -1) {
                // printf("LAST CHAR\n");
                newChar = '*';
            }

            // produce item in buffer
            // printf("produce char: %c\n", newChar);

            // printf("waiting on mutex...\n");
            sem_wait(&mutex);
            
            // add item to buffer
            q_enqueue(shared_q, newChar);

            // printf("signalling mutex...\n");
            sem_post(&mutex);

            if (result == -1) {
                doBreak = 1;
                break;
            }
        }

        // printf("signalling full...\n");
        sem_post(&full);
        if (doBreak) break;
        
    }
    // printf("closing...\n");
    close(fp);
} 

void *consumerThread (void *arg){
    int doBreak = 0;

     while(1){

        // printf("\t\t\t\tC: waiting on full...\n");
        sem_wait(&full);

        while (!isEmpty(shared_q)) {

            // printf("\t\t\t\tC: waiting on mutex...\n");
            sem_wait(&mutex);

            // remove item from buffer to buffer
            char nextChar = q_dequeue(shared_q);

            // printf("\t\t\t\tC: signalling mutex...\n");
            sem_post(&mutex);

            // printf("\t\t\t\tC: signalling empty...\n");
            sem_post(&empty);


            // consume next item in buffer
            // printf("\t\t\t\tC: consume char: '%c'\n", nextChar);
            printf("%c", nextChar);
            fflush(stdout);
            if (nextChar == '*'){
                doBreak = 1;
                break;
            }
            sleep(1);
        }

        
        if (doBreak) break;

        

    }
}


/**** Circular Queue ****/


int isEmpty(queue *q) {
    return q->front == -1;
}

int isFull(queue *q) {
    return q->size == q->maxSize;
}

void display(queue *q)
{
    int i;
    // if (isEmpty(q)) {
    if (0) {
        printf("\n\t\tEmpty Queue\n");
    }
    else
    {
        printf("\n\t\tFront: '%c' (%d)", q->items[q->front], q->front);
        printf("\n\t\tItems: ");
        for(i = q->front; i != q->rear; i=(i+1) % q->maxSize) {
            printf("%c ", q->items[i]);
        }
        printf("%c ", q->items[i]);
        printf("\n\t\tRear: '%c' (%d)", q->items[q->rear], q->rear);
        printf("\n\t\tSize: %d \n", q->size);
    }
}


void q_enqueue(queue *q, char data) {
    if (isFull(q)){
    // if (0){
        printf("Queue full!\n");
    }
    else {
        // display(q);
        if (q->front == -1) {
            q->front = 0;
        }
        q->rear = (q->rear + 1) % q->maxSize;
        q->items[q->rear] = data;
        q->size++;
        // printf("\n\t\tInserted: '%c'\n", data);
        // display(q);
    }
}

char q_dequeue(queue *q) {
    if (isEmpty(q)) {
        printf("Queue empty!\n");
        return '\0';
    }
    else {
        char item = q->items[q->front];
        if (q->front == q->rear) {
            q->front = -1;
            q->rear = -1;
        }
        else {
            q->front = (q->front + 1) % q->maxSize;
        }
        q->size--;
        // printf("\n\t\tRemoved: '%c'\n", item);
        // display(q);
        return item;
    }
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

    /***** Threads *****/

    pthread_t tidP;     /* process id for producer thread */
    pthread_t tidC;     /* process id for consumer thread */

    sem_init(&mutex, 1, 1);
    sem_init(&full, 1, 0);
    sem_init(&empty, 1, CAPACITY);

    pthread_attr_t attr[1];     /* attribute pointer array */
    fflush(stdout);
    
    /* Required to schedule thread independently.*/
    pthread_attr_init(&attr[0]);
    pthread_attr_setscope(&attr[0], PTHREAD_SCOPE_SYSTEM);  
    /* end to schedule thread independently */
    
    /* Create the threads */
    pthread_create(&tidP, NULL, &producerThread, NULL);
    pthread_create(&tidC, NULL, &consumerThread, NULL);

    /* Wait for the threads to finish */
    pthread_join(tidP, NULL);
    pthread_join(tidC, NULL);

    sem_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    // Terminate threads
    pthread_exit(NULL);


    // Detach segments
    if (shmdt(shared_q) == -1){
      perror("shmdt");
      exit(-1);
    }
    
    // Deallocate segments
    shmctl(shmid, IPC_RMID, NULL);
    

    printf("\nEnd of program.\n");
}