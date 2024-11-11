T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 배열 크기, M: 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열

    max_flies = 0  # 최대 파리 수 초기화

    # 슬라이딩 윈도우로 M x M 영역에 대해 파리 수 계산
    for i in range(N - M + 1):  # i: 행의 시작 인덱스
        for j in range(N - M + 1):  # j: 열의 시작 인덱스
            flies = 0
            # M x M 영역에서 파리 수 합산
            for x in range(M):
                for y in range(M):
                    flies += arr[i + x][j + y]

            # 최대 파리 수 갱신
            max_flies = max(max_flies, flies)

    # 결과 출력
    print(f"#{t} {max_flies}")