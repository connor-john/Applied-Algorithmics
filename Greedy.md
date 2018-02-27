### Problem Statement 1: Computing GCD (as GreedyGCDProblem)

Read in a sequence of 32-bit signed integers (several per line separated by spaces) until a single line
containing zero (0). There will be at most 1000 integers per line. For each line except for the last one,
compute the greatest common divisor (gcd) of that set of integers. Then output on a line the statement
“The gcd of the integers is x.” where x is the desired gcd. Note, for this problem, all answers should
be non-negative.

The input should be taken from keyboard/stdin/System.in.

Sample Input:  
2 4 8  
15 0 -5  
6 20 25 5 30  
28 21952 49 294 3822  
0  

The precisely formated output should be sent to console/stdout/System.out.

Sample Output:  
The gcd of the integers is 2.  
The gcd of the integers is 5.  
The gcd of the integers is 1.  
The gcd of the integers is 7.  


### Problem Statement 2: Minimum Double Pair (as GreedyPairProblem)

The input format for this problem is the same as in Problem 1 but all integers (per line) are assumed to
be different. We read in a sequence of 32-bit signed integers (several per line separated by spaces) until
a single line containing zero (0). For each line except for the last one, compute the smallest sum s such
that there are two different pairs of integers (x1, x2) and (y1, y2), where x1 < x2, x1 6= y1 < y2 6= x2,
that both sum to s (e.g., x1 + x2 = y1 + y2 = s). If such a sum s is possible, output on a line “yes: s”.
Otherwise output on a line “None”.

The input should be taken from keyboard/stdin/System.in.

Sample Input:  
2 1 3 4  
10 20 40 45 5 15 25  
24 23 8 29 31 5  
10 20 50 51 52 53 54 12 15 16  
0  

The output should be sent to console/stdout/System.out.

Sample Output:  
yes: 5  
yes: 25  
None  
yes: 62  
