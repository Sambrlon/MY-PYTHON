n = int(input("Введите число:"))

def febonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)

print(febonacci(n))