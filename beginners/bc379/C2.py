def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    count = 0
    
    for i in range(M):
        Ai = A[i]

        if i == 0 and X[i] - 1 > 0: 
            return -1 

        if i == M - 1:
            count += (N - A[X[i]])
            break

        if Ai > X[i+1] - X[i]: return -1
        
        count += (X[i+1] - X[i])
    
    return count

if __name__ == "__main__":
    print(main())