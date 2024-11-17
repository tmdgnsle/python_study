T = int(input())

for test_case in range(1, T+1):
    a, b = input().split()
    if a * len(b) != b * len(a):
        result = 'no'
    else:
        result = 'yes'
    print(f'#{test_case} {result}')