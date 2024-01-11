The total memory usage of an array can be determined using the `sizeof()` operator.

**Example:**
```
int A[] = {10, 23, 11, 63, -55, 99, -20, 88};
printf("%d", (int) sizeof(A));
```

The total memory allocated of an array can be calculated using the formula:

$$\text{Total Memory} = \text{dimension} \times n_\text{elements} \times n_\text{bytes}$$

> `int A[8] = {10, 23, 11, 63, -55, 99, -20, 88};`  
> The total size of `A` is not 8 (this is the number of elements).  
> The total size of `A` is $1 \times 8 \times 4 = 32$.  
> Since `A` is one-dimensional, the $\text{dimension}$ of `A` is 1.
 
### Memory Size of Data Types

The $n_\text{bytes}$ can be retrived from the table below.

| Data Type | Size (32-bit) |
|-----------|---------------|
| char      | 1 byte        |
| int       | 4 bytes       |
| long      | 8 bytes       |
| float     | 4 bytes       |
| double    | 8 bytes       |
| pointer   | 8 bytes       |