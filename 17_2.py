f = open("17_2.txt")
m = [int(x) for x in f]

red = 0
green = 0
blue = 0

colors = 0
c = []

for i in range(len(m) - 2):
    if (m[i] == 255) and (m[i + 1] == 0) and (m[i+2] == 0):
        colors += 1
        red += 1
        c.append((m[i], m[i+1], m[i+2]))
    elif (m[i] == 0) and (m[i + 1] == 255) and (m[i+2] == 0):
        colors += 1
        green += 1
        c.append((m[i], m[i + 1], m[i + 2]))
    elif (m[i] == 0) and (m[i + 1] == 0) and (m[i+2] == 255):
        colors += 1
        blue += 1
        c.append((m[i], m[i + 1], m[i + 2]))

print(c)

print(colors, max(red, green, blue))


