#!/bin/python3

import sys


def great_cons_prod(n,k,num):
    max_pro=0
    for i in range(n-k+1):
        product=1
        for j in range(i,i+k):
            product*=int(num[j])
        max_pro = max(max_pro,product)
    return max_pro
        

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(great_cons_prod(n,k,num))
