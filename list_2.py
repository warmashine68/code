Primes = [2, 3, 5, 7, 11, 13, 17]#turn 3-13
'''Primes[1:3] = [5]# берется срез, он "выкидывается" и заменяется на 5
print(Primes)
Primes[:]=[1,0]# берем весь список И заменяем его на 1 и 0
print(Primes)
'''
part = Primes[1:6]
part = part[::-1]
Primes[1:6] = part
print(Primes)
# Мы внутри списка перевернули срез
