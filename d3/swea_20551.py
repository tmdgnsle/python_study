T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    cnt = 0
    if C < 3 or B < 2 or A < 1:
        cnt = -1
    else:
        while C <= B:
            B -= 1
            cnt += 1
        while B <= A:
            A -= 1
            cnt += 1

    print(f'#{test_case} {cnt}')