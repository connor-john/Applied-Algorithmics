### Problem Statement: Which digit? (as DivideConquerProblem)

A single positive integer i is given. Write a program to find the digit located in position i in the following
infinite sequence of digits created by juxtaposing the increasing larger sequences of incremented integers
1, 2, 3, . . .. For example, the first 80 digits of the sequence are as follows:

11212312341234512345612345671234567812345678912345678910123456789101112345678910

The first line of the input (stdin/keyboard) contains a single integer n (1 ≤ n ≤ 100), the number of
test cases, followed by one line for each test case. The line for a test case contains the single integer i
(1 ≤ i < 10^10).

There should be one output line per test case containing the digit located in position i.

Sample input:  
3  
8  
3  
21  

Sample output:  
2  
2  
6  
