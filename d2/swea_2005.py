T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    a = []
    count = 0
    while count < n:
        a.append([])
        if count == 0:
            a[count].append(1)
        if count != 0:
            for i in range(count+1):
                if i == 0:
                    a[count].append(1)
                elif i == count:
                    a[count].append(1)
                else:
                    a[count].append(a[count-1][i-1] + a[count-1][i])
        count += 1
    print(f'#{test_case}')
    for i in a:
        for j in i:
            print(j, end=' ')
        print()