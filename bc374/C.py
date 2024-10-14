N = int(input())
K = list(map(int, input().split()))

total = sum(K)
ans = float("inf")

for i in range(1<<N):
    a,b= 0,0
    for j in range(N):
        print(i,j)
        if (i >> j) & 1:
            a += K[j]
        else:
            b += K[j]
    ans = min(ans, max(a,b))

print(ans)