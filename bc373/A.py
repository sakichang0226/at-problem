S = [input() for i in range(12)]
count = 0

for i in range(len(S)):
    if i + 1 == len(S[i]):
        count += 1

print(count)