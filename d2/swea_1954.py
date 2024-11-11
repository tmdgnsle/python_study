def generate_snail_matrix(n):
    # n x n 크기의 2차원 배열을 생성하고, 0으로 초기화
    matrix = [[0] * n for _ in range(n)]

    # 방향은 오른쪽, 아래, 왼쪽, 위 순으로 설정
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, direction = 0, 0, 0  # 시작 위치 및 방향
    num = 1  # 시작 숫자

    while num <= n * n:
        matrix[x][y] = num
        num += 1

        # 다음 위치를 계산
        nx, ny = x + dx[direction], y + dy[direction]

        # 범위를 벗어나거나 이미 숫자가 채워진 경우, 방향을 변경
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        # 위치 갱신
        x, y = nx, ny

    return matrix


def print_snail_matrix(matrix, case_number):
    print(f"#{case_number}")
    for row in matrix:
        print(" ".join(map(str, row)))


# 입력
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    snail_matrix = generate_snail_matrix(N)
    print_snail_matrix(snail_matrix, t)