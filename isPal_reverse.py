'''
Нерекурсивный метод, просто сравниваем с перевернутым масивом
либо так, либо используя reverse, где reverse:
def reverse(S):
    return S[::-1]
'''
def isPal(A): #ababa
    if A == A[::-1]:
        return True
    else:
        return False
s = input()
s = list(s)
print(isPal(s))
# Доделать в рекурсивном варианте, 11 урок Ханойскии башни 35,01!!!!!!
