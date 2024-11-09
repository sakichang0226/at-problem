def main():
    N,K = map(int, input().split())
    S = list(input())

    count = 0
    ecount = 0
    for i in range(N):
        if (S[i] == "X"):
            count = 0
            continue
        
        count += 1
    
        if (count == K):
            count = 0
            ecount += 1

    
    return ecount

if __name__ == "__main__":
    print(main())


