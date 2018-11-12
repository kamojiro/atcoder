N, K = map( int, input().split())
L = K*2
KK = [[0]*L for _ in range(L)]

for i in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == "B":
        x, y = x%L, y%L
    else:
        x, y = (x+K)%L, (y+K)%L
    if 0 <= x < K-1:
        if 0 <=y < K-1:
            KK[0][0] += 1
            KK[x][y] += 1
            KK[0][y] -= 1
            KK[x][0] -= 1
            KK[x+K][y+K] += 1
            KK[L-1][L-1] += 1
            KK[x+K][L-1] -= 1
            KK[L-1][y+K] -= 1
        else:
            KK[x][y] += 1
            KK[0][y-K]
            
