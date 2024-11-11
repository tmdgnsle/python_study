T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    multiply = []
    if N > M:
        for i in range(N-M+1):
            sumAB = 0
            for j in range(M):
                sumAB += A[i+j]*B[j]
            multiply.append(sumAB)
    else:
        for i in range(M-N+1):
            sumAB = 0
            for j in range(N):
                sumAB += A[j]*B[i+j]
            multiply.append(sumAB)
    print(f'#{test_case} {max(multiply)}')