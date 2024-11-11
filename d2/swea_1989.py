T = int(input())

for test_case in range(1, T+1):
    word = input()
    a = 0
    reverse_word = word[::-1]
    if word == reverse_word:
        a = 1
    print(f'#{test_case} {a}')