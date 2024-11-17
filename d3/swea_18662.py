import math
T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(float, input().split())
    results = []
    first = C - 2*B +A
    if first < 0:
        results.append(-first)
    else:
        results.append(first)
    second = (C-A)/2 - B
    if second < 0:
        results.append(-second)
    else:
        results.append(second)

    print(f'#{test_case} {math.floor(min(results) * 10) / 10}')