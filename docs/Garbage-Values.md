# Garbage Values

Undetermined values inside a [[Memory]] location.

> `int x;`
> > Since `x` is undefined, it will be initially filled with a garbage value. Until `x` is initialized.
> `int x = 0;`
> > Now `x` is initialized with a value therefore it does not have garbage values inside it anymore.

## Declaration and Definition

On **[[Array-Declaration]]**, the [[Array]] will be filled with garbage values, but during the **definition** it will be filled with the initialized values.