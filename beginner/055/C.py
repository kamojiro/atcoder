N, M = map( int, input().split())
if M <= N*2:
    print(N)
else:
    print(N+(M-N*2)//4)
