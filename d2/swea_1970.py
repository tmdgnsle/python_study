T = int(input())

for test_case in range(1, T+1):
    arr = []
    N = int(input())
    arr.append(N//50000)
    N = N%50000
    arr.append(N // 10000)
    N = N % 10000
    arr.append(N // 5000)
    N = N % 5000
    arr.append(N // 1000)
    N = N % 1000
    arr.append(N // 500)
    N = N % 500
    arr.append(N // 100)
    N = N % 100
    arr.append(N // 50)
    N = N % 50
    arr.append(N // 10)
    N = N % 10
    print(f'#{test_case}')
    for m in arr:
        print(m, end=' ')
    print()