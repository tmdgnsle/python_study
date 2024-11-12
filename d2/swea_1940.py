T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vel, distance = 0,0
    for ar in arr:
        if ar[0] == 0:
            distance += vel
        elif ar[0] == 1:
            vel += ar[1]
            distance += vel
        elif ar[0] == 2:
            if vel < ar[1]:
                vel = 0
            else:
                vel -= ar[1]
            distance += vel
    print(f'#{test_case} {distance}')