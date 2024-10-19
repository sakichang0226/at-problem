N,Q = map(int, input().split())
L,R = 1,2
count = 0

def migimawari(point, move, cp):
    conflict = False
    mc = 0

    if(point == move):
        return conflict, 0

    while ((move != point) and not conflict):
        point = point + 1  if point + 1 <= N  else 1
        mc += 1

        if(point == cp):
            conflict = True
    
    return conflict, mc


def hidarimawari(point, move, cp):
    conflict = False
    mc = 0

    if(point == move):
        return conflict, 0

    while ((move != point) and not conflict):
        point = point - 1  if point - 1 > 0  else N
        mc += 1

        if(point == cp):
            conflict = True

    return conflict, mc

"""
    右回り > 左回り
    左回り > 右回り
    右回り > 左回り　コンフリクト
    左回り > 右回り　コンフリクト
"""
def judge(s1,s2,c1,c2):
    
    if (s2 > s1 and not c1):
        return s1
    elif (s1 > s2 and not c2):
        return s2
    elif (s2 > s1 and c1):
        return s2
    elif (s1 > s2 and c2):
        return s1
    elif (s1 == s2):
        return s1
    
    return 0

for i in range(Q):
    hands, move = input().split()
    move = int(move)
    
    if (hands == "R"):
        conflict1, s1 = migimawari(R, move, L)
        conflict2, s2 = hidarimawari(R, move, L)

        count += judge(s1,s2,conflict1,conflict2)

        R = move
    
    if (hands == "L"):
        conflict1, s1 =  migimawari(L, move, R)
        conflict2, s2 =  hidarimawari(L, move, R)

        count += judge(s1,s2,conflict1,conflict2)

        L = move

print(count)

