#Great state about lists in the functions
def f():
    A[0] = 7 # We can change one element at the list
def f_2():
    A = [5, 5] # But we can't change the whole array(==list) using function
A = [1, 2, 3]
f()
print(A)
f_2()
print(A)

#________________________________
del A #http://radio-hobby.org/modules/instruction/python/54-instruktsiya-del

#a*x*x + b*x + c = 0 function(developing)
from math import sqrt
def Solve(a, b, c):
    D = b*b - 4*a*c
    if(D < 0):
        return False
    elif (D == 0):
        return (-1 * b) / (2*a)
    elif (D > 0):
        return ((-1*b+sqrt(D))/(2*a)), ((-1*b-sqrt(D))/(2*a)) 

a_i = int(input())
b_i = int(input())
c_i = int(input())

print(Solve(a_i, b_i, c_i))

