abc = [int(i)  for i in list(input())]
bca = abc[1] * 100 + abc[2] * 10 + abc[0]
cab = abc[2] * 100 + abc[0] * 10 + abc[1]

print(str(bca) + " " + str(cab))

