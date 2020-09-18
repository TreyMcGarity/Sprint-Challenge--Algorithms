#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) it's linear because it loops once and stops depending on n's value.


b) O(n^2) its a nested loop and each loop runs n times and nesting runs exponential because its for each n runs n times.


c) O(n) it's linear because the recursive function runs once for "bunnites" value times.

## Exercise II
Base Cases are
1) the floors we are dropping eggs on
2) if egg breaks or not
3) Stop one floor below lowest egg breaking floor

I would implement a binary search algorithm: 

Starting at the middle floor and drop the egg
    If one floor remaining,
        return floor
    If it does break go to bottom half, 
        recall until it doesn't break. 
    If it doesnt break, 
        we move to upper half
        recall until it doesn't break.

runtime complexity = O(log(n)) because binary searches are O(log(n))