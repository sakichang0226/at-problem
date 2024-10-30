S = list(input())
T = list(input())
N = len(S)
X = []

i = 0

for i in range(N):
    if(S[i] > T[i]):
        S[i] = T[i]
        X.append(S[:])

for i in range(N - 1, -1, -1):
    if(T[i] > S[i]):
        S[i] = T[i]
        X.append(S[:])

print(len(X))
for x in X:
    print("".join(x))