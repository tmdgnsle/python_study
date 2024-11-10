T = int(input())

for test_case in range(1, T+1):
    A, B, N = input().split()
    A = int(A)
    B = int(B)
    N = int(N)
    small = A if A <= B else B
    big = B if A <= B else A
    count = 0
    while small <= N:
        if small > big:
            small, big = big, small
        small += big
        count += 1
    print(count)