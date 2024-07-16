f = open("17_1.txt")
m = [int(x) for x in f]

count2 = 0
s = 0

for i in range(len(m) - 1):
    if (m[i] < 0) and (m[i + 1] > 0):
        count2 += 1
        s += m[i]

print(count2, s)
