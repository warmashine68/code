def appen(S, el):
    S[len(S)] = el
    return S
S = []
for i in range(0, 5):
    S[i] = int(input())

S = appen(S, input())
print(S)
