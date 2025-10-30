def sum_natural_numbers(n):
    if n<1:
        return 0
    return(n*(n+1))//2
value = 2
result = sum_natural_numbers(value)
print(f"the sum of first {value} natural numbers is " ,result)