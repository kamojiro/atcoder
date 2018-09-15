from itertools import accumulate

def E(i, x):
    if i == 1:
        return 5*i
    return (2*i+1)*x

N, X = map( int, input().split())
G = list( map( int, input().split()))
accG = accumulate(G)
accG = accG.insert(0,0)
ans = X*2*N + G[-1]*N*5
for k in range(N):
    
    
