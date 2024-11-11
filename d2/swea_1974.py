def is_valid_sudoku(grid):
    # 행과 열 검증
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if grid[i][j] in row or grid[j][i] in col:
                return 0
            row.add(grid[i][j])
            col.add(grid[j][i])

    # 3x3 격자 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set()
            for k in range(3):
                for l in range(3):
                    num = grid[i + k][j + l]
                    if num in block:
                        return 0
                    block.add(num)

    return 1


# 입력 처리 및 결과 출력
T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(9)]
    result = is_valid_sudoku(grid)
    print(f"#{t} {result}")