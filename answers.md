# CMPS 2200 Recitation 06
## Answers
**Name:** Jamari Ross

Place all written answers from `recitation-07.md` here for easier grading.


- **2)** If $n = 0 or 1$, the function returns a base case, otherwise, the work for the function can be represented as: $F(n) = F(n-1) + F(n-2) + O(1)$, where $F(n-1)$ is the first part of the recursive call, $F(n-2)$ is the second part of the recursive call, and $O(1)$ represents the (time to get the) sum.
.
- Thus, the work is $O(2^n)$.

.
- **3)** When $n = 0 or 1$ (base cases) the span is $O(1)$, but when $n > 1$, it runs two recursive equations. These calls are not independent, so they must be ran sequentially, therefore we get: $S(n)=S(n−1)+O(1)$, which after being solved gives the time complexity
.
$S(n) = O(n)$

.
- **4)** The counts help demonstrate how this approach is not efficient. Something that I noticed was how at each step, there is a large amount of unnecessary work being done and how there is a "reversed" Fibonacci pattern that's shows up. Smaller values are computed numerous times, while large values are computed significantly less.
.

- **6)** fib_top_down is called at most once for every value because we compute $Fi$, then future calls for the same value will just return the stored/cached value. So unique calls = $O(n)$
.
Therefore, work & span = $O(n)$
.

- **8)** Since fib_bottom_up is solved iteratively, we call two calls of fibonacci values. Therefore, each value is called up to two times, one for the first recursive call, and once for the second.
.
Since each iteration does constant work and the implementation is sequential, both work and span = $O(n)$
