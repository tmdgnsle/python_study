T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    s = input()
    if N %2 != 0:
        result = 'No'
    elif s[:N//2] == s[N//2:]:
        result = 'Yes'
    else:
        result = 'No'
    print(f'#{test_case} {result}')