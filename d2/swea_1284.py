T = int(input())

for test_case in range(1, T+1):
    P,Q,R,S,W = map(int, input().split())
    A = P * W
    B = Q + (W-R)*S if W > R else Q
    result = A if A < B else B
    print(f'#{test_case} {result}')