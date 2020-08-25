def factorial(n):
    result = n
    for i in range(n, 1, -1):
        result *= i - 1
    return result


n = int(input())

result = factorial(n)

print(result)
