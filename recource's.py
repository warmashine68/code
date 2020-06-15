#recources
#the main idea of this program is that n! = n*(n-1)!
def fact(n):
    if n == 1:
        return 1 #to stop the recource
    else:
        return n*(fact(n-1)) #the program works in reverse, we use like(5! = (((1*2)*3)*4)*5 in reverse)-> n -= 1 -> smaller and smaller while n == 1
num = int(input())
print(fact(num))
'''
5! = 5*4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! (1! = 1 -> ...) = 5 * 4 * 3 * 2 * 1
Происходит расстановка как в стеке, тогда ....
Сперва мы находим, что
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1, затем мы возвращаемся назад подставляя значения и удаляем предыдущие стопки -> answer
'''
