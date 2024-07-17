f = open("17_3.txt")
m = [int(x) for x in f]

sequence = [0, 1]
z = 0
zz = 1
while zz <= 10000:
    new = z + zz
    sequence.append(new)
    z = zz
    zz = new

all_sequences = []
current_sequence = []

for i in range(len(m)):
    if m[i] in sequence:
        current_sequence.append(m[i])
    elif 1 < len(current_sequence):
        all_sequences.append(current_sequence)
        current_sequence = []

print(len(all_sequences), sum(max(all_sequences)))
