T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())

    result = 0

    for i in range(1, N+1):
        result += i
        if result == P:
            result -= 1

    print(result)