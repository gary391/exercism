def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))
"""
def recursive_function(parameters):
    if base_case_condition:
        return base_result
    else:
        return recursive_function(modified_parameters)
        
        
"""
"""
12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
"""

"""
check e/o:
    Base case:
        even //2 == 1 
    - if even 
        - (even // 2) --> check e/o 
    - else:
        - (odd * odd +1) --> check e/o
        
12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
"""
def rec_fun(number):
    def helper(num, count):
        count+=1
        if num % 2 == 0:
            num = num // 2
            if num == 1:
                return count
            else:
                return helper(num, count)
        else:
            num = (num * 3) + 1
            return helper(num, count)
    return helper(number, 0)
print(rec_fun(1))