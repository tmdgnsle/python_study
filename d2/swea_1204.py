
T = int(input())

for test_case in range(1, T+1):
    test_case_number = int(input())
    score_list = list(map(int, input().split()))
    count_list = [0 for _ in range(101)]
    for score in score_list:
        count_list[score] += 1

    max_count = max(count_list)
    result = 0

    # 뒤에서부터 탐색하여 max_count의 가장 큰 인덱스를 찾음
    for i in range(100, -1, -1):
        if count_list[i] == max_count:
            result = i
            break
    print(f'#{test_case_number} {result}')


