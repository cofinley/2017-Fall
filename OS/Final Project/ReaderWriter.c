/* 
    OS Final Project 
    Group 4
      Abhimanyu Dakwale, Raymond Lian, Connor Finley
    2017/11/07
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
#include <string.h>
#include <inttypes.h>

// Shared file
#define FILENAME "mytest.dat"

// Define/assert maximum number of readers and writers
#define MAX_WRITERS 6
#define MAX_READERS 3

// Semaphores
sem_t readerLock, writerLock, readAttempt, resourceLock;

// Counters
int readcount, writecount = 0;

// Array of strings to use for individual writers
// Simulates multiple writers all having different payloads
// The strings cannot exceed the maximum number of writers
char writerArray[MAX_WRITERS][20]={
    "Papa culo", 
    "And sheperds we", 
    "shall be", 
    "my lord", 
    "for thee", 
    "power has"
}; 


void *readerThread (void *arg){

    // Reader

    // Get thread id (reader number)
    int id = (intptr_t) arg;
    int fileCursor = 0;
    char newChar;
    FILE* fp;
    

    while(1) {

        // Attempt to read (blocked by any writer)
        sem_wait(&readAttempt);

        // Try to sign in reader
        sem_wait(&readerLock);
        readcount++;
        if(readcount == 1){
            // If first reader, try to get access to resource for all readers
            sem_wait(&resourceLock);
        }

        // Release semaphores so other readers can sign in/out
        sem_post(&readerLock);
        sem_post(&readAttempt);

        // Read (one char at a time; round robin with other readers)
        fp = fopen(FILENAME, "r");
        // Update new file position for readers
        // Otherwise, each reader would start at the beginning of the file
        fseek(fp, fileCursor, SEEK_SET);

        // Process char read in from file
        int result = fscanf(fp, "%c", &newChar);

        // Update file position for next read
        fileCursor++;

        // Pretty printing
        if (result != -1) {
            printf("%*c", id, ' ');
            printf("Reader (%d), reading: %c\n", id, newChar);
        }

        fclose(fp);

        // END Read

        // Try to sign reader out
        sem_wait(&readerLock);
        --readcount;
        if(readcount == 0){
            // If last reader, relinquish resource for other threads
            sem_post(&resourceLock);
        }
        
        // Allow other readers to sign in/out
        sem_post(&readerLock);

        if (result == -1) {
            // EOF; terminate thread
            pthread_exit(NULL);
        }

        // Sleep to allow other threads to work
        sleep(1);
    }
}


void *writerThread (void *arg){

    // Writer

    // Get thread id (writer  number)
    int id = (intptr_t) arg;
    FILE* fp;
    char buffer[] = "were all one in the same ";

    // Try to add new writer count
    sem_wait(&writerLock);
    writecount++;
    if(writecount == 1){
        // If there is a writer, block all read attempts
        sem_wait(&readAttempt);
    }

    //Copy the text the writer thread will write from the global string array
    strcpy(buffer, writerArray[id-1]);

    // Pretty printing
    printf("\t\t\t");
    printf("%*c", id, ' ');
    printf("Writer (%d), writing: %s\n", id, buffer);

    // Allow other writers to write
    sem_post(&writerLock);

    // Critical section, hold onto resource
    sem_wait(&resourceLock);

    // Write; do it all at once
    fp = fopen(FILENAME, "a+");
    fprintf(fp, "%s", buffer); //write into the file
    
    fclose(fp);

    // END Write

    // Release resource for other writers
    sem_post(&resourceLock); 
    sleep(1);

    // To to sign-out writer
    sem_wait(&writerLock); 
    writecount--;          
    if(writecount == 0){
        // Last writer should open up availability for other threads
        sem_post(&readAttempt);
    }

    // Allow other writers to sign in/out
    sem_post(&writerLock);
    
    // Terminate thread
    pthread_exit(NULL);
}


void resetFile() {
    // House-keeping function to start from clean slate each run

    FILE* fp = fopen(FILENAME, "w");
    char s[] = "Hi!";
    char* c;
    for (c = s; *c != '\0'; c++){
        fprintf(fp, "%c", *c);
    }
    fclose(fp);
}


void main(){

    printf("program started \n");
    resetFile();

    // Initialize all semaphores with value of 1
    sem_init(&readerLock, 1, 1);
    sem_init(&writerLock, 1, 1);
    sem_init(&readAttempt, 1, 1);
    sem_init(&resourceLock, 1, 1);

    // // Create attribute pointer array
    pthread_attr_t attr[1];

    // Required to schedule thread independently
    pthread_attr_init(&attr[0]);
    pthread_attr_setscope(&attr[0], PTHREAD_SCOPE_SYSTEM);  
    // end to schedule thread independently

    /* Create and execute the reader threads dynamically */
    pthread_t r_thread_id[MAX_READERS];
    int j;
    for (j=0; j < MAX_READERS; j++) {
        // Pass in index to thread to use as id
        pthread_create(&r_thread_id[j], &attr[0], readerThread, (void *)(intptr_t)j+1);
    }

    /* Create and execute the writer threads dynamically */
    pthread_t w_thread_id[MAX_WRITERS];
    int i;
    for (i=0; i < MAX_WRITERS; i++) {
        // Pass in index to thread to use as id
        pthread_create(&w_thread_id[i], &attr[0], writerThread, (void *)(intptr_t)i+1);
    }

    /* Clean up threads once they are terminated */
    for (i=0; i < MAX_WRITERS; i++){
        pthread_join(w_thread_id[i], NULL);
    }

    for (j=0; j < MAX_READERS; j++){
        pthread_join(r_thread_id[j], NULL);
    }

    // Remove semaphores
    sem_destroy(&readerLock);
    sem_destroy(&writerLock);
    sem_destroy(&readAttempt);
    sem_destroy(&resourceLock);

    printf("\nEnd of program.\n");
}
