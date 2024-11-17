T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    result = -1
    for i in range(N-K+1):
        arr = a[i:i+K]
        if result == -1:
            result = max(arr) - min(arr)
        elif result > max(arr) - min(arr):
            result = max(arr) - min(arr)
    print(f'#{test_case} {result}')