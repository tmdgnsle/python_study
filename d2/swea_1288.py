T = int(input())


for test_case in range(1, T + 1):
    a= input()
    arr1=[]
    k=1

    while (len(arr1)<10):
        b=int(a)*k
        b=str(b)
        for i in b:
            if i not in arr1:
                arr1.append(i)
        k+=1
    print(f'#{test_case} {int(b)}')
