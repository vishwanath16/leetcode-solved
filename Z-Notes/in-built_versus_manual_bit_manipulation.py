import time
import random


def hammingWeight_string_based(n):
    return list(bin(n)[2:]).count("1")

def hammingWeight_bitwise(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def generate_large_number():
    bits = 10**6  
    binary_str = ''.join(random.choice('01') for _ in range(bits))  
    return int(binary_str, 2)


n = generate_large_number()


start = time.time()
result1 = hammingWeight_string_based(n)
end = time.time()
print(f"String-based solution result: {result1}, Time taken: {end - start:.6f} seconds")


n = generate_large_number()  
start = time.time()
result2 = hammingWeight_bitwise(n)
end = time.time()
print(f"Bitwise solution result: {result2}, Time taken: {end - start:.6f} seconds")
