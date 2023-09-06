import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total_sum=0
    def sum_of_multiples(n):
        def sum_of_multiples_up_to(n, multiple):
            num_terms = (n - 1) // multiple
            last_term = num_terms * multiple
            return num_terms * (multiple + last_term) // 2
    
        sum_3 = sum_of_multiples_up_to(n, 3)
        sum_5 = sum_of_multiples_up_to(n, 5)
        sum_15 = sum_of_multiples_up_to(n, 15)
    
        total_sum = sum_3 + sum_5 - sum_15
        return total_sum
    print(sum_of_multiples(n)) 
