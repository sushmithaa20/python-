import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = n * (n+1) //2
    sqre_sum = sum ** 2
    sum_Sqr = n  * (n+1) * (2 *n +1) // 6
    diff  = abs(sqre_sum-sum_Sqr)
    print(diff)
