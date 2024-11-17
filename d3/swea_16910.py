T = int(input())

for test_case in range(1, T+1):
    count = 0
    N = int(input())
    for x in range(N+1):
        for y in range(N+1):
            if x**2 + y**2 <= N**2:
                count += 1
    result = 4*(count - N -1) +1
    print(f'#{test_case} {result}')