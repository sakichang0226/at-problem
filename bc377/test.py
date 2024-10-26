N,M = map(int, input().split())
islands = [list(map(int, input().split())) for i in range(M)] 
visited = [[0 for j in range(N)] for i in range(M)]

def search(y, x, visited):
    if (y < 0 or y > M - 1 or x < 0 or x > N - 1):
        return 

    if (visited[y][x] == 1):
        return 
    
    visited[y][x] = 1

    if islands[y][x] == 0:
        return

    search(y-1, x, visited)
    search(y+1, x, visited) 
    search(y, x - 1, visited)
    search(y, x + 1, visited)

def main():
    count = 0
    for i in range(M):
        for j in range(N):
            if islands[i][j] == 1:
                if (visited[i][j] == 0) :
                    count += 1
                
                search(i-1, j, visited)
                search(i+1, j, visited)
                search(i, j - 1, visited)
                search(i, j + 1, visited)

    print(count)

main()