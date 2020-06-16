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
l = input()
l = list(l)
#print(isPal(l))
# Терминальное условие - сравниваем часть строки с срезом в рекурсивом варианте
def isPal_rec(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal_rec(s[1:-1])

print(isPal_rec(l))
