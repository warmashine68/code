s = input() # Нужно поменять половинки местами
if len(s) % 2 == 0:
    part = len(s) // 2
else:
    print("It's impossible")
    quit()
s1 = s[:part]
s2 = s[part:]
print(s2 + s1)
