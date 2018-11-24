from itertools import accumulate
N, K = map( int, input().split())
A = list( map( int, input().split()))
accA = [0] + list( accumulate(A))
V = [1]*(N*(N+1)//2)
ans = 0
check = False
for i in range(40,-1,-1):
    W = [0]*(N*(N+1)//2)
    for l in range(N):
        for r in range(l+1,N+1):
            if V[l*(2*N+1-l)//2+r-l-1] == 0:
                continue
            if (accA[r]-accA[l])%(2**(i+1)) >= 2**i:
                W[l*(2*N+1-l)//2+r-l-1] = 1
    if check == False:
        if sum(W) >= K:
            check == True
        else:
            continue
    if sum( V and W) >= K:
        ans += 2**i
        V = V and W
print(ans)

    


