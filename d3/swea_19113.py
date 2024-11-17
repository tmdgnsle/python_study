
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    result = []
    i = 0
    while prices:
        if (prices[i] // 3)*4 in prices:
            result.append(str(prices[i]))
            prices.remove((prices[i] // 3) * 4)
            prices.remove(prices[i])
        else:
            i += 1
    print(f'#{test_case}', " ".join(result))