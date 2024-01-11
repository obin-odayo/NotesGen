#include <stdio.h>

int main(){
    // array declared only
    int a[10];   // array data type  int
                 // array name       a
                 // array size       10
    
    // the print result for a are the memory addresses allocated for a since only garbage values are inside it.
    // array a is not defined yet.
    printf("\n=====\nArray a:\n");
    for (int i = 0; i < 10; i++){printf("%d\n", a[i]);}

    // ==========
    // array with most elements defined
    int b[3] = {1,2};   // array data type  int
                        // array name       b
                        // array size       10
                        // elements defined {1,2}
    
    // the print result for element 0 and 1 are the actual values inside b. But since element 2 is undefined the memory location is the printed value.
    printf("\n=====\nArray b:\n");
    for (int i = 0; i < 3; i++){printf("%d\n", b[i]);}
    
    // ==========
    // simultanous declaration of array
    char nameA[100], nameB[100];   // array data type   char
                                   // array names       nameA, nameB
                                   // array sized       100, 100
    return 0;
}