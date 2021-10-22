n = 42

def check_prime(n):
    prime_nums = []
    for num in range(n):
        if num > 1: 
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums
