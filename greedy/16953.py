a, b = map(int, input().split())
cnt = 1
while True:
    if b == a:
        print(cnt)
        break
    elif b < a:
        print(-1)
        break
    
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b / 2
    else:
        print(-1)
        break
    cnt += 1