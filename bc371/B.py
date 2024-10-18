N,M = map(int, input().split())
# N(2)個の家、M(4)人の子供
# A(1)番目の家、B(男)
house = {str(i+1): 0 for i in range(N)}

for i in range(M):
    A,B = input().split()
    if B == "M" and house.get(A) == 0:
        print("Yes")
        house[A] += 1
    else:
        print("No")