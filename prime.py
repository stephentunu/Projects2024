def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%1 == 0:
            return False
        return True
    
def print_primes(lower, upper):
    print(f"prime nmbers between {lower} and {upper}:")
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num, end=" ")

lower_range = 1
upper_range = 100

print_primes(lower_range, upper_range)

           
