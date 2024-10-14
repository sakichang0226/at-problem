N = int(input())
K = list(map(int, input().split()))

for i in range(1<<N):
    a,b= [],[]
    for j in range(N):
        if i & (1 << j):
            a.append(K[j])
        else:
            b.append(K[j])
    print(a,b)