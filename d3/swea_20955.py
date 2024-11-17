T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    S = input().strip()  # 시작 문자열
    E = input().strip()  # 목표 문자열

    possible = False  # 결과 변수

    # 역방향으로 탐색
    while len(E) >= len(S):
        if E == S:
            possible = True
            break

        if E[-1] == 'X':  # 마지막 문자가 'X'라면 제거
            E = E[:-1]
        elif E[-1] == 'Y':  # 마지막 문자가 'Y'라면 제거 후 뒤집기
            E = E[:-1][::-1]

    # 결과 출력
    if possible:
        print(f"#{test_case} Yes")
    else:
        print(f"#{test_case} No")