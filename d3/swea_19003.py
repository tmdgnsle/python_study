T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    pelindrom =  []
    result = 0
    for i in range(N):
        word = input()
        if word == word[::-1]:
            pelindrom.append(word)
        else:
            arr.append(word)

    if arr:
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i][::-1] == arr[j]:
                    result += 2*M
    if pelindrom:
        result += M

    print(f'#{test_case} {result}')
