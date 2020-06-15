#Testing a number to a simple
def isSimple(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

num = int(input())
print(isSimple(num))
