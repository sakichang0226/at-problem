N = int(input())
a = list(map(int, input().split()))

def is_odd_number(a): 
    for v in a:
        if v % 2 != 0:
            return True

    return False

def calc(a):
    return [v / 2 for v in a]

def check_max_count(a):
    count = 0

    while not is_odd_number(a):
        count += 1
        a = calc(a)

    return count

print(check_max_count(a))