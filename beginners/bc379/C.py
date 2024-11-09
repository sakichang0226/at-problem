def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    A = list(map(int, input().split()))
   
    stones = [0 for i in range(N)]
    count = 0

    for i in range(M):
        stones[X[i] - 1] = A[i]

    for i in range(N - 1, 0, -1): 
        if i <= 0:
            break

        if stones[i] <= 0: 
            count += 1 - stones[i]
            stones[i - 1] -= (1 - stones[i])

    if stones[0] <= 0:
        return -1
    
    return count

if __name__ == "__main__":
    print(main())