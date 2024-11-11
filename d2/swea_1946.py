T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = ''
    for i in range(N):
        letter, number = input().split()
        number = int(number)
        a += letter * number
    result = [a[i:i+10] for i in range(0, len(a), 10)]
    print(f'#{test_case}')
    for s in result:
        print(s)