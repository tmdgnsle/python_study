T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    s = input().split()
    t = input().split()
    Q = int(input())
    results = []
    for i in range(Q):
        n = int(input())
        index_s = (n-1)%N
        index_t = (n-1)%M
        result = s[index_s] + t[index_t]
        results.append(result)
    # print(f'#{test_case}', end=' ')
    # for i in range(Q):
    #     print(results[i], end=' ')
    print(f"#{test_case}", " ".join(results))

