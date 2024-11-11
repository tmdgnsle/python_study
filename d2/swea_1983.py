def calculate_grade(score, N):
    # 학점 리스트
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # N명의 학생을 10등분하여 평점 부여
    return grades[score // (N // 10)]


# 테스트 케이스 입력
T = int(input())

for t in range(1, T + 1):
    # N(학생 수), K(학점을 알고 싶은 학생 번호)
    N, K = map(int, input().split())

    # 각 학생의 점수 (중간, 기말, 과제 점수)
    students = []
    for i in range(N):
        mid, final, homework = map(int, input().split())
        total_score = mid*0.35 + final*0.45 + homework*0.2
        students.append((total_score, i + 1))  # (총점, 학생 번호)

    # 총점 순으로 내림차순 정렬
    students.sort(reverse=True, key=lambda x: x[0])

    # K 번째 학생의 점수에 해당하는 인덱스를 찾고 그 점수로 학점 계산
    for idx, (score, student_id) in enumerate(students):
        if student_id == K:
            grade = calculate_grade(idx, N)
            print(f"#{t} {grade}")
            break