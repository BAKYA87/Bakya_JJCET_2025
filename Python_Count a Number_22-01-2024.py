'''
#Given an integer N, write a program to count the number of digits in N.

#Input Format

#Example 1: Input0: N = 12345

#Example 2: Input1: N = 8394

#Constraints

#n <= 10000

#Output Format

#Output0: 5 Explanation: N has 5 digits

#Output1: 4 Explanation: N has 4 digits

#Sample Input 0

#12345
#Sample Output 0

#5
#Sample Input 1

#876349
#Sample Output 1

#6
'''
______________________________________________
1. N=int(input())
   string=str((N))
   print(int(len(string)))

2.def count_digits(N);
       return len(str(N))
    N=12345
    output=count_digits(N)
    print(output)
       