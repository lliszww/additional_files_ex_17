f = open("17_3.txt")
m = [int(x) for x in f]

sequence = [1, 2]
z = 1
zz = 2
while zz <= 10000:
    new = z + zz
    sequence.append(new)
    z = zz
    zz = new

all_sequences = []
current_sequence = []

for i in range(len(m) - 1):
    if m[i] in sequence:
        first_index = sequence.index(m[i])
        current_sequence.append(m[i])
    elif len(current_sequence) != 0:
        all_sequences.append(current_sequence)
        current_sequence = []

print(len(all_sequences), sum(max(all_sequences)))


