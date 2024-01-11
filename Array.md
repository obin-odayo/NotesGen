# Array

A data structure variable that stores **groups** of elements of the data that are [[homogenous]].

Elements are stored in [[contiguous]] memory which is [[static]]ally allocated.

Common types of Arrays:  

1. List: for **one-dimensional** array.
2. Table: for **two-dimensional** array.

## Accessing Elements

To access [[elements]] inside an array use the **[[indexing operation]]**.

Arrays are initially filled with [[garbage values]] until values are initialized.

An [[illegal memory access]] occurs when the index of an indexing operation is **outside the range of the array**.

> `int A[8] = {10, 23, 11, 63, -55, 99, -20, 88};`
> > To access 10 in `A`: `A[0]`  
> > To access 23 in `A`: `A[1]`  
> > Array indexing always starts at 0

To determine the size of the array in the [[memory]]  the `sizeof` operator can be used.
