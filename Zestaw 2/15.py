def check_pow_sum(n, N):
    copy_n = n
    suma = 0
    while copy_n > 0:
        digit = copy_n % 10
        suma += digit**N
        copy_n //= 10

    return (suma == n)

print(check_pow_sum(153, 3))

N = int(input())
for i in range(10**(N-1),10**N):
    if check_pow_sum(i, N):
        print(i)