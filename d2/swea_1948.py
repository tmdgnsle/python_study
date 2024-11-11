T = int(input())

for test_case in range(1, T+1):
    first_month, first_day, second_month, second_day = map(int, input().split())
    result = 0
    for month in range(first_month, second_month):
        if month == 2:
            result += 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            result += 30
        else: result += 31

    print(f'#{test_case} {result - first_day + second_day + 1}')