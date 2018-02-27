"""
Connor Taylor
Compsci 320 Assignment1
Finds the GCD for each line of intergers(up to 1000 integers)
"""

import sys

def get_integers():
    integer_string = str(sys.stdin.readline())
    integers_list = integer_string.split()
    if integers_list == ["0"]:
        return False
    else:
        return integers_list

def euclidean_alg(a,b):
    while b !=0:
        (a,b) = (b, a % b)
    return abs(a)

def main():
    integers = get_integers()
    if integers and len(integers) == 1:
        print("The gcd of the integers is ",str(integers[0]),".", sep = "")
        main()
    elif integers:
        start = int(integers[0])
        second = 1
        stop = len(integers)
        while second != stop and start != 1:
            start = euclidean_alg(start,int(integers[second]))
            second += 1
        print("The gcd of the integers is ", str(start),".", sep= "")
        main()
    else:
        pass

main()
