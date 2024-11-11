T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    rotate_arr = [[] for _ in range(N)]
    for i in range(N):
        rotate = ''
        for j in range(N-1, -1, -1):
            rotate += arr[j][i]
        rotate_arr[i].append(rotate)

    for i in range(N-1, -1, -1):
        rotate =''
        for j in range(N-1, -1, -1):
            rotate += arr[i][j]
        rotate_arr[-i-1].append(rotate)

    for i in range(N-1, -1, -1):
        rotate = ''
        for j in range(N):
            rotate += arr[j][i]
        rotate_arr[-i-1].append(rotate)

    print(f'#{test_case}')
    for i in range(N):
        for j in range(3):
            print(rotate_arr[i][j], end=' ')
        print()