T = int(input())

for test_case in range(1, T+1):
    L, R = map(int, input().split())
    if R+1 <= 2*L -1:
        result = 'yes'
    else:
        result = 'no'
    print(result)