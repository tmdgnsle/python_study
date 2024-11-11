T = int(input())

for test_case in range(1, T+1):
    first_hour, first_minute, second_hour, second_minute = map(int, input().split())
    hour = first_hour + second_hour
    minute = first_minute + second_minute
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print(f'#{test_case} {hour} {minute}')