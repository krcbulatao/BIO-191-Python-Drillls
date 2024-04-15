size = 5

first = []
for j in range(size - 1):
    first.append("*" * size)
first.append("*" * size)

two = []
for j in range(size - 1):
    if j == 0:
        two.append("*" * size)
    else:
        two.append("*" + ((size - 2) * " ") + "*")
two.append("*" * size)

for f, t in zip(first, two):
    print(f + '\t' + t)