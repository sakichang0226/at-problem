A = list(map(int, input().split()))
colors = [0,0,0,0]

for i in A:
    colors[i-1] += 1

count = 0

for c in range(4):
    count += int(colors[c] / 2) 

print(count)