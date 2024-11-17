import math
def hapsung(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return True
    return False


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    x = N+4
    y = 4
    while not hapsung(x) or not hapsung(y):
        x += 1
        y += 1

    print(f'#{test_case} {x} {y}')