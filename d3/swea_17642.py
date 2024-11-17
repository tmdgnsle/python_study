T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split())

    result = 0
    diff = B-A
    if  diff > 1:
        result = diff // 2
    elif diff == 1 or diff < 0:
        result = -1
    elif diff == 0:
        result = 0
    print(f'#{test_case} {result}')