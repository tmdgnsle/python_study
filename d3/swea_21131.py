T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    base = [i + 1 for i in range(N)]
    change_arr = [arr[i][0] for i in range(N)]
    cnt = 0

    for i in range(N - 1, -1, -1):
        if arr[0][i] != base[i]:

            for k in range(i + 1):
                arr[0][k], change_arr[k] = change_arr[k], arr[0][k]
            cnt += 1
    print(cnt)