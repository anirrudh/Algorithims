/*
This C++ program will be used to demonstrate the
insertion-sort algorithim as described in the book, 
Introduction to Algorithims
*/

#include <stdio.h>
#include <math.h>
#include <iostream>
#include <ctime> 

using namespace std; 

int * randomArray() {
    static int  a[10] = {0};
    srand((unsigned)time(0));

    for(int i=0; i<10; ++i){ 
        a[i] = rand() % 10 + 1; 
    } 
    return a; 
}


void printArray(int arr[], int size) {
    int i;
    for (i=0; i < size; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() 
{
    cout << "Here is an example of insertion sort in C++ :" << endl; 
    int *p;
    p = randomArray();
    static int  arr[9] = {0};
    for ( int k = 0; k < 9; k++ ) {
       arr[k] = *(p + k);
    }
    
    int size = sizeof(arr)/sizeof(arr[0]); 
    cout << "Scrambled Array: " << endl;
    printArray(arr, size);   
    
    for(int j = 1; j < size; ++j){
        int key = arr[j];
        int i = j - 1;
        while(i >= 0 && arr[i] > key){
            arr[i+1] = arr[i];
            i = i - 1;
            
  
        }
        arr[i+1] = key;   
    }
    cout << "Sorted Array: " << endl;
    printArray(arr, size);
}

