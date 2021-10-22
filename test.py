from collections import OrderedDict

temp = []
temp_result = []
f = []
alpha = ['A', 'B', 'C', 'D']
INPUT = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

temp.append(alpha[0])

for i in INPUT:
    for idx, j in enumerate(i):
        if j == 1:
            temp.append(alpha[INPUT.index(i)] + alpha[idx])

for i in range(0, len(temp)):
    temp[i] = ''.join(sorted(temp[i]))
    temp[i] = ''.join(OrderedDict.fromkeys(temp[i]))

temp0 = []
for value in temp:
    if value not in temp0:
        temp0.append(value)

print(temp0)
temp2 = []
temp = temp0.copy()

while True:
    temp0 = temp.copy()
    a = len(temp2)
    for i in temp0:
        if i == temp0[0]:
            continue
        for j in i:
            k = alpha.index(j)
            for idx, l in enumerate(INPUT[k]):
                if l == 1:
                    str = i + alpha[idx]
                    str = ''.join(sorted(str))
                    str = ''.join(OrderedDict.fromkeys(str))
                    temp.append(str)
    for value in temp:
        if value not in temp2:
            temp2.append(value)
    b = len(temp2)
    if b == a:
        break
print(temp2)

f = [0] * len(temp2)

for i in INPUT:
    for idx, j in enumerate(i):
        if j == 1:
            str = alpha[INPUT.index(i)] + alpha[idx]
            str = ''.join(sorted(str))
            str = ''.join(OrderedDict.fromkeys(str))
            f[temp2.index(str)] = 1
temp_result.append(f)

for i in temp2:
    f = [0] * len(temp2)
    if i == temp2[0]:
        continue
    for j in i:
        k = alpha.index(j)
        for idx, l in enumerate(INPUT[k]):
            if l == 1:
                str1 = i + alpha[idx]
                str1 = ''.join(sorted(str1))
                str1 = ''.join(OrderedDict.fromkeys(str1))
                if str1 != i:
                    f[temp2.index(str1)] = 1
    temp_result.append(f)

for i in temp_result:
    print(i)
