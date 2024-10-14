def main():
    S = input()
    T = input()

    s = len(S)
    t = len(T)

    max_len = t if s > t else s

    for i in range(0, max_len):
        if (S[i] != T[i]):
            return i+1
    
    return 0 if s == t else max_len + 1

if __name__ == '__main__':
    print(main())
