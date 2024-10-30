N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
element = 0
i = 0

for j in range(N):
    element = A[i][j] - 1 if i >= j else A[j][i] - 1
    i = element

print(element + 1)