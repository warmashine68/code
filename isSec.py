#Является ли число n точной степенью двойки
def isSec(n):
    if n==2:
        return True
    elif n%2 != 0:
        return False
    else:
        return(isSec(n/2))
    
num = int(input())
print(isSec(num))
