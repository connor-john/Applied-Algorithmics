### Problem statement: Maximum Evaluation (ignoring precedence) (as DynamicProblem)

Given an expression using only * and + binary operators and integer operands we want to “evaluate
it” such that we obtain the largest possible result. For our task we do not follow the usual arithmetic
precedence of doing multiplication (denoted by *) before addition (denoted by +). 

For example, 5 + 3 * 2 can be evaluated as (with parentheses used to denote operator ordering):  
(5+3) * 2=16  
or  
5+(3 * 2)=11  

Input will be one line containing a positive integer n, followed by n lines of test expressions, each with
at least 1 and at most 200 operators. Each operator and operand is separated by at least one space
character. For each case, output the maximum evaluation value over all possible operator orderings.
Each integer in the input expression can fit in a 32-bit word. However, note you may need to use a
multi-precision data type (e.g., BigInteger ) to express some of the answers for the harder test data.

Sample Input:  
3  
5 + 3 * 2  
100 * 100 + 100 * 100 * 100 + 100 * 100  
-1 + -4 * -3  

Sample Output:  
16  
40000000000  
15  
