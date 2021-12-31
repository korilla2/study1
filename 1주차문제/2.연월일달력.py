T = int(input())


for i in range(T):
    a = list(str(input()))
    month = int(a[4]+a[5])
    day = int(a[6]+a[7])
    if (month < 1) or (month > 12):
        print(f'#{i+1} -1')
    elif (month == 2) and ((day < 1) or (day > 28)):
        print(f'#{i+1} -1')
    elif (month in [1, 3, 5, 7, 8, 10, 12]) and ((day < 1) or (day > 31)):
        print(f'#{i+1} -1')
    elif (month in [4, 6, 9, 11]) and ((day < 1) or (day > 30)):
        print(f'#{i+1} -1')
    else:
        print(f'#{i+1} {a[0]+a[1]+a[2]+a[3]}/{a[4]+a[5]}/{a[6]+a[7]}')
