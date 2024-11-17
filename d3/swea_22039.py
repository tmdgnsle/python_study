def fibonacci_partition(n):
    # 최대 N까지의 피보나치 수열을 계산하여 저장합니다.
    max_n = 100
    fib = [0] * (max_n + 1)
    fib[1] = 1
    if max_n > 1:
        fib[2] = 1
    for i in range(3, max_n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    results = []

    # 피보나치 수들의 합을 계산합니다.
    total_sum = sum(fib[1:n + 1])

    # 만약 총합이 홀수라면 불가능
    if total_sum % 2 != 0:
        results.append("impossible")

    else:
        # 목표는 총합의 절반
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        # 부분합을 찾기 위한 DP
        for i in range(1, n + 1):
            for j in range(target, fib[i] - 1, -1):
                if dp[j - fib[i]]:
                    dp[j] = True

            # 만약 부분합이 불가능하면
        if not dp[target]:
            results.append("impossible")

        else:
            # 부분합을 만들 수 있다면 역추적하여 집합을 나눔
            answer = ['B'] * n
            w = target
            for i in range(n, 0, -1):
                if w >= fib[i] and dp[w - fib[i]]:
                    answer[i - 1] = 'A'
                    w -= fib[i]
            results.append("".join(answer))

    return results

# 입력 예제
T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    result = fibonacci_partition(N)
    for res in result:
        print(res, end='')
    print()