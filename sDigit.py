#Дано число, нужно вернуть сумму цифр этого числа
def sDigit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sDigit(n//10)
num = int(input())
print(sDigit(num))
