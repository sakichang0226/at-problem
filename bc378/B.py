N = int(input())
garbage = [list(map(int, input().split())) for i in range(N)]
Q = int(input())

for i in range(Q):
    t,d = map(int, input().split())
    q = garbage[t - 1][0]
    r = garbage[t - 1][1]
    
    k = 0 if d % q == r else  (r - d) % q

    print(k + d)