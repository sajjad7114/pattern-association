def read(filename, p):
    arr = []
    with open(filename, 'r') as f:
        s = f.read().split()
        for line in s:
            for point in line:
                if point == p:
                    arr.append(1)
                else:
                    arr.append(0)
    return arr


w = []
for i in range(63):
    w.append([0]*166)
alph = ['a', 'b', 'c', 'd', 'e', 'j', 'k']

for a in alph:
    for i in range(1, 4):
        filename = 'data/' + a + str(i) + '.txt'
        filename2 = 'data2-noisy/' + a + str(i) + '.txt'
        arr = read(filename, '*')
        arr2 = read(filename2, '1')
        for j in range(63):
            if arr[j] == 1:
                w[j][0] += 1
                for k in range(165):
                    if arr2[k] == 1:
                        w[j][k+1] += 1

test = 'c1'
file = 'data/' + test + '.txt'
arr = read(file, '*')
file2 = 'data2-noisy/' + test + '.txt'
arr2 = read(file2, '1')
output = []
for i in range(63):
    y_in = -w[i][0]
    for j in range(165):
        y_in += arr2[j] * w[i][j+1]
    if y_in > 0:
        output.append('*')
    else:
        output.append('.')

for i in range(9):
    for j in range(7):
        print(output[i*7 + j], end='')
    print('    ', end='')
    for j in range(7):
        if arr[i*7 + j] == 1:
            print('*', end='')
        else:
            print('.', end='')
    print()
