T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T + 1):
    s = input().strip()  # 각 테스트 케이스 문자열 입력
    max_length = 10  # 마디의 최대 길이

    # 마디 길이를 1부터 10까지 차례로 확인
    for length in range(1, max_length + 1):
        pattern = s[:length]  # 현재 길이로 마디 추출
        repeated_pattern = pattern * (30 // length + 1)  # 패턴을 30보다 크게 반복

        # 원본 문자열의 처음 30자리와 비교
        if repeated_pattern[:30] == s:
            print(f"#{t} {length}")
            break