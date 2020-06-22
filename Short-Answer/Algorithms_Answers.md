#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The number of operations-->(runtime) will increase at a linear rate as the size of the input increases-->(the n). ===>{O(n)}


b)runtime complexity will be " O(n^n) " because the snippet will have nested loops. operations will increase quadratically


c)this will also be O(n) like the fisrt one but it will for each value (its like a mix of the 1st 2 but no loop)

## Exercise II

I would loop through the building floors as if they were as 1 sorted array with the 2nd floor  on the top of first, third floor on the top of 2nd an so on as if this was in binary search tree.

I would start in the middle(n/2) of the "array or list"(mid = arr[len(arr)-1 // 2] ) also save spot(checkpoint = len(mid)-1) which will also be the next top floor and we will check the middle of that array also,so I will
drop the egg and {{ if egg=="broken"}} then move down 1, check again, an so on.

 solving the issue by log(f) to reach the base case(2eggz).

 ps: even from knee height from the ground, the eggs will break(in real life), but I get the simulation?.