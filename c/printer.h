#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define RND 10


void printArray(int arr[], int size)
{
    printf("{ ");
    for(int i=0; i<size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("}\n");
}


void shuffle(int arr[], int size)
{
    if (size > 1)
    {
        int i;
        for (i = 0; i < size - 1; i++)
        {
            int j = rand() % RND;
            const int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
}
