N,C = map(int, input().split())
T = list(map(int, input().split()))
count = 1
t = T[0]

for i in range(1,len(T)):
    if T[i] - t >= C : 
        count += 1
        t = T[i]

print(count)