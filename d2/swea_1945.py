T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0,0,0,0
    while N % 2 == 0:
        a += 1
        N = N // 2
        # print(N)
    while N % 3 == 0:
        b += 1
        N = N // 3
        # print(N)
    while N % 5 == 0:
        c += 1
        N = N // 5
    while N % 7 == 0:
        d += 1
        N = N // 7
    while N % 11 == 0:
        e += 1
        N = N // 11

    print(f'#{test_case} {a} {b} {c} {d} {e}')