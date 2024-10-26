def check(y, x, l_y, l_x, board, visited):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return
    
    if (not (y == l_y and x != l_x) and not (x == l_x and y != l_y)):
        return 
    
    if visited[y][x] == 1:
        return
    
    visited[y][x] = 1

    if board[y][x] == ".":
        board[y][x] = "x"

    check(y + 1, x, l_y, l_x, board, visited)
    check(y - 1, x, l_y, l_x, board, visited)
    check(y, x - 1, l_y, l_x, board, visited)
    check(y, x + 1, l_y, l_x, board, visited)

def main():
    board = [[j for j in input()] for i in range(8)] 

    for i in range(8):
        for j in range(8):
            if board[i][j] == "#":
                visited = [[0 for j in range(8)] for i in range(8)]
                check(i, j+1, i, j, board, visited)
                check(i, j-1, i, j, board, visited)
                check(i-1, j, i, j, board, visited)
                check(i+1, j, i, j, board, visited)

    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == ".":
                count += 1

    return count

if __name__ == "__main__":
    print(main())