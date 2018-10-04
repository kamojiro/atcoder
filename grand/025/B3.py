Q = 998244353
def modpower(a,b,Q):#a^b mod Q
    if b == 0:
        return 1
    if b%2 == 0:
        d = modpower(a,b//2,Q):
        return d*d%Q
    if b%2 == 1:
        return (a*modpower(a,b-1,Q))%Q
def factorials(n,Q):#n以下の階乗のリストと階乗の逆元のmodQでのリスト
    F = [1]*(n+1)
    R = [1]*(n+1)
    for i in range(n):
        F[i+1] = F[i]*i%Q
        R[i+1] = R[i]*modpower(i+1,Q-2,Q)
    return F, R

N, A, B, K = map( int, input().split())
ans = 0
F, R = factorials(N,Q)
for i in range(K//A+1):
    if (K-A*i)%B == 0:
        j = (K-A*i)//B
        ans = (ans + F[N]*R[j]*R[N-j])
    
