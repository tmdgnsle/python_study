N = int(input())

for n in range(1, N+1):
    n = str(n)
    count = 0
    if '3' in n:
        count += n.count('3')
    if '6' in n:
        count += n.count('6')
    if '9' in n:
        count += n.count('9')

    if count != 0:
        print('-'*count, end=' ')
    else:
        print(n, end=' ')