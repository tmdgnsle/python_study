T = int(input())

for test_case in range(1, T+1):
    S, K = input().split()
    if int(K) == 0:
        result = S.index('o')
    elif S[1] == 'o':
        if int(K)%2==0:
            result = 1
        else:
            result = 0
    else:
        if int(K)%2==0:
            result = 0
        else:
            result = 1
    print(f'#{test_case} {result}')