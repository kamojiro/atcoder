from collections import Counter
def find(x, A):
    p = A[x]
    if p == x:
        return x
    a = find(p, A)
    A[x] = a
    return a

N, K, L = map( int, input().split())
V = [ i for i in range(N)]
W = [ i for i in range(N)]
for _ in range(K):
    p, q = map( int, input().split())
    p, q = p-1, q-1
    bp, bq = find(p,V), find(q,V)
    V[q] = bp
    V[bq] = bp

for _ in range(L):
    r, s = map( int, input().split())
    r, s = r-1, s-1
    br, bs = find(r,W), find(s,W)
    W[s] = br
    W[bs] = br

for i in range(N):
    find(V[i], V)
    find(W[i], W)
ans = 0
VW = [ (V[i], W[i]) for i in range(N)]
CVW = Counter(VW)
ANS = [0]*N
for i in range(N):
    ANS[i] = CVW[(V[i],W[i])]

print(' '.join( map( str, ANS)))
    
