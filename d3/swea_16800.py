import math

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            arr.append(i)
    x = arr[-1]
    y = N // x
    distance = x + y - 2
    print(f'#{test_case} {distance}')