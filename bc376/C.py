N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

x = 0
B.append(x)
t = 0

while(ans < N or t < N):
    for i in A:
        for j, k in enumerate(B):
            if k >= i:
                B[j] -= i
                ans += 1
                break 
    
    print(ans)
    t += 1

print(ans)