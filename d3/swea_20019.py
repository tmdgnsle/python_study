T = int(input())

for test_case in range(1, T+1):
    s = input().strip()
    if s == s[::-1]:
        part = s[0:(len(s)-1)//2]
        if part == part[::-1]:
            result = 'YES'
        else:
            result = 'NO'
    else:
        result = 'NO'
    print(f'#{test_case} {result}')