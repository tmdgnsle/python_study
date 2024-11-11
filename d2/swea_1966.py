T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = ''
    for i in sorted(arr):
        sorted_arr += str(i) + ' '
    print(f'#{test_case} {sorted_arr}')